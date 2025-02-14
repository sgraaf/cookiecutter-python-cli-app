from pathlib import Path
from shutil import rmtree

import nox

nox.options.sessions = ["pre-commit", "tests", "docs"]
nox.options.default_venv_backend = "uv|virtualenv"
nox.options.reuse_existing_virtualenvs = True
nox.options.error_on_external_run = True

ALL_PYTHON_VERSIONS = [
    # [[[cog
    # import re
    # for line in open("pyproject.toml"):
    #     if (match := re.search(r"Programming Language :: Python :: (?P<version>3\.\d+)", line)) is not None:
    #         cog.outl(f'"{match.group("version")}",')
    # ]]]
    "3.9",
    "3.10",
    "3.11",
    "3.12",
    "3.13",
    # [[[end]]]
]

# [[[cog
# import yaml
# rtd = yaml.safe_load(open(".readthedocs.yaml"))
# cog.outl(f'DOCS_PYTHON_VERSION = "{rtd["build"]["tools"]["python"]}"')
# ]]]
DOCS_PYTHON_VERSION = "3.13"
# [[[end]]]

ROOT_DIR = Path(__file__).resolve().parent
VENV_DIR = ROOT_DIR / ".venv"

DOCS_DIR = ROOT_DIR / "docs"
DOCS_SOURCE_DIR = DOCS_DIR
DOCS_BUILD_DIR = DOCS_DIR / "_build" / "html"

PACKAGE_BUILD_DIR = ROOT_DIR / "build"
PACKAGE_DIST_DIR = ROOT_DIR / "dist"


@nox.session(python=False)
def dev(session: nox.Session) -> None:
    """Sets up a Python development environment for the project."""
    # create the development environment (venv)
    session.run(
        "uv",
        "venv",
        "--seed",
        "--prompt",
        "{{ cookiecutter.app_name }}",
        str(VENV_DIR),
        external=True,
        silent=True,
    )

    # install the current package in editable mode (along with its dependencies)
    session.run(
        "uv",
        "pip",
        "install",
        "--editable",
        ".[dev]",
        env={"VIRTUAL_ENV": str(VENV_DIR)},
        external=True,
        silent=True,
    )


@nox.session
def cog(session: nox.Session) -> None:
    """Run cog."""
    session.install("cogapp", "PyYAML", ".")

    cog_input_files = ["noxfile.py", "README.md", "docs/cli.md"]
    for cog_input_file in cog_input_files:
        session.run("cog", *session.posargs, "-r", cog_input_file)

    session.notify("pre-commit", ["trailing-whitespace", "--files", *cog_input_files])


@nox.session(name="pre-commit")
def pre_commit(session: nox.Session) -> None:
    """Run pre-commit hooks."""
    # fmt: off
    args = session.posargs or [
        "--all-files",  # run on all the files in the repo.
    ]
    # fmt: on
    session.install("pre-commit-uv")
    session.run("pre-commit", "run", *args)


@nox.session(python=ALL_PYTHON_VERSIONS, tags=["tests"])
def tests(session: nox.Session) -> None:
    """Run tests."""
    session.install(".[tests]")
    session.run("pytest", *session.posargs)


@nox.session(python=DOCS_PYTHON_VERSION)
def docs(session: nox.Session) -> None:
    """Builds and tests the docs."""
    session.install(".[docs]")

    # create a temporary directory to store the doctrees
    tmp_dir = session.create_tmp()

    for builder in ["html", "doctest"]:
        # fmt: off
        session.run(
            "python", "-m", "sphinx",
            "-T",  # display full traceback when an exception occurs
            "-E",  # rebuild the environment
            "-W", "--keep-going",  # turn warnings into errors, but continue to the end of the build
            "-b", builder,  # selects a builder
            "-d", str(Path(tmp_dir) / "doctrees"),  # directory to save doctree pickles
            "-D", "language=en",  # set language
            str(DOCS_SOURCE_DIR),  # source directory
            str(DOCS_BUILD_DIR),  # output directory
        )
        # fmt: on
    session.run("python", "-m", "doctest", "README.md")


@nox.session(name="docs-live", python=DOCS_PYTHON_VERSION)
def docs_live(session: nox.Session) -> None:
    """Builds and serves the docs with hot reloading on file changes."""
    # fmt: off
    args = session.posargs or [
        "--open-browser",  # open the browser after building documentation
        str(DOCS_SOURCE_DIR),  # source directory
        str(DOCS_BUILD_DIR),  # output directory
    ]
    # fmt: on

    session.install(".[docs]")
    session.install("sphinx-autobuild")

    session.run("sphinx-autobuild", *args)


@nox.session(name="clear-packages", python=False)
def clear_packages(session: nox.Session) -> None:  # noqa: ARG001
    """Remove build and dist directories."""
    if PACKAGE_BUILD_DIR.is_dir():
        rmtree(PACKAGE_BUILD_DIR)
    if PACKAGE_DIST_DIR.is_dir():
        rmtree(PACKAGE_DIST_DIR)


@nox.session(name="build-package", python=False)
def build_package(session: nox.Session) -> None:
    """Builds the package, both as a source distribution (sdist) and as a wheel."""
    args = session.posargs or ["--out-dir", PACKAGE_DIST_DIR, ROOT_DIR]
    session.run("uv", "build", *args)


@nox.session(name="upload-package")
def upload_package(session: nox.Session) -> None:
    """Builds the package, both as a source distribution (sdist) and as a wheel."""
    # check whether the package's long description will render correctly on PyPI
    session.run("uvx", "twine", "check", "--strict", f"{PACKAGE_DIST_DIR.as_posix()}/*")

    # upload the package(s) to (Test)PyPI
    session.run("uv", "publish", *session.posargs, f"{PACKAGE_DIST_DIR.as_posix()}/*")


@nox.session(name="release-to-testpypi", python=False)
def release_to_testpypi(session: nox.Session) -> None:
    """Clears, builds and uploads the package to TestPyPI."""
    session.notify("clear-packages")
    session.notify("build-package")
    session.notify("upload-package", ["--repository", "testpypi"])


@nox.session(name="release-to-pypi", python=False)
def release_to_pypi(session: nox.Session) -> None:
    """Clears, builds and uploads the package to PyPI."""
    session.notify("clear-packages")
    session.notify("build-package")
    session.notify("upload-package")
