import shutil
import subprocess
import sys


def possibly_install_uv() -> None:
    if shutil.which("uv") is None:
        # install uv
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "--user", "uv"], check=False
        )


def possibly_install_nox() -> None:
    if shutil.which("nox") is None:
        # possibly install uv
        possibly_install_uv()

        # install nox
        subprocess.run(["uv", "tool", "install", "nox"], check=False)


def possibly_install_pre_commit() -> None:
    if shutil.which("pre-commit") is None:
        # possibly install uv
        possibly_install_uv()

        # install pre-commit
        subprocess.run(
            ["uv", "tool", "install", "pre-commit", "--with", "pre-commit-uv"],
            check=False,
        )


def initialize_git_repository() -> None:
    # initialize Git repository
    subprocess.run(["git", "init", "-b", "main"], check=False)

    # update and install pre-commit hooks
    subprocess.run(["pre-commit", "autoupdate"], check=False)
    subprocess.run(["pre-commit", "install", "--install-hooks"], check=False)

    # add files
    subprocess.run(["git", "add", "."], check=False)

    # run nox "cog" and "pre-commit" sessions
    subprocess.run(["nox", "--session", "cog", "pre-commit"], check=False)

    # possibly re-add files
    subprocess.run(["git", "add", "."], check=False)

    # commit
    subprocess.run(
        [
            "git",
            "commit",
            "-m",
            ":cookie: Initial commit from `cookiecutter-python-cli-app`",
        ],
        check=False,
    )


def initialize_venv() -> None:
    # run nox "dev" session
    subprocess.run(["nox", "--session", "dev"], check=False)


if __name__ == "__main__":
    # possibly install nox (and uv)
    possibly_install_nox()
    # possibly install pre-commit (and uv)
    possibly_install_pre_commit()
    # perform git initialization
    if "{{ cookiecutter.init_git }}" == "True":
        initialize_git_repository()
    # create venv and install dependencies
    if "{{ cookiecutter.init_venv }}" == "True":
        initialize_venv()
