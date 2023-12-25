import shutil
import subprocess
import sys


def possibly_install_pipx() -> None:
    if shutil.which("pipx") is None:
        # install pipx
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "--user", "pipx"], check=False
        )
        # add pipx to PATH
        subprocess.run([sys.executable, "-m", "pipx", "ensurepath"], check=False)


# possibly install nox (and pipx)
if shutil.which("nox") is None:
    # possibly install pipx
    possibly_install_pipx()

    # install nox
    subprocess.run([sys.executable, "-m", "pipx", "install", "nox"], check=False)

# possibly install pre-commit (and pipx)
if shutil.which("pre-commit") is None:
    # possibly install pipx
    possibly_install_pipx()

    # install pre-commit
    subprocess.run([sys.executable, "-m", "pipx", "install", "pre-commit"], check=False)

# perform git initialization
if "{{ cookiecutter.init_git }}" == "True":
    # initialize Git repository
    subprocess.run(["git", "init", "-b", "main"], check=False)

    # update and install pre-commit hooks
    subprocess.run(["pre-commit", "autoupdate"], check=False)
    subprocess.run(["pre-commit", "install", "--install-hooks"], check=False)

    # add files
    subprocess.run(["git", "add", "."], check=False)

    # run nox "cog" and "pre_commit" sessions
    subprocess.run(["nox", "--session", "cog", "pre_commit"], check=False)

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

# create venv and install dependencies
if "{{ cookiecutter.init_venv }}" == "True":
    # run nox "dev" session
    subprocess.run(["nox", "--session", "dev"], check=False)
