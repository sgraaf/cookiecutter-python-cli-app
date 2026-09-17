import shutil
import subprocess
import sys
from functools import partial

run = partial(subprocess.run, check=False)


def possibly_install_pipx() -> None:
    if shutil.which("pipx") is None:
        # install pipx
        run([sys.executable, "-m", "pip", "install", "--user", "pipx"])
        # add pipx to PATH
        run([sys.executable, "-m", "pipx", "ensurepath"])


def possibly_install_uv() -> None:
    if shutil.which("uv") is None:
        # possibly install pipx
        possibly_install_pipx()

        # install uv
        run([sys.executable, "-m", "pipx", "install", "uv"])


def initialize_venv() -> None:
    # create virtual environment and install dependencies
    run(["uv", "sync", "--dev"])


def initialize_git_repository() -> None:
    # initialize Git repository
    run(["git", "init", "-b", "main"])

    # update and install pre-commit hooks
    run(["uv", "run", "prek", "update"])
    run(["uv", "run", "prek", "install", "--prepare-hooks"])

    # add files
    run(["git", "add", "."])

    # run the pre-commit hooks (which, amongst others, runs cog)
    run(["uv", "run", "prek", "run", "--all-files"])

    # possibly re-add files
    run(["git", "add", "."])

    # commit
    run(
        [
            "git",
            "commit",
            "-m",
            "Initial commit from `cookiecutter-python-cli-app`",
        ],
    )


if __name__ == "__main__":
    # possibly install uv (and pipx)
    possibly_install_uv()
    # create venv and install dependencies
    initialize_venv()
    # perform git initialization
    if "{{ cookiecutter.init_git }}" == "True":
        initialize_git_repository()
