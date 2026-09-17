# Contributing

Thank you for your interest in contributing to *{{ cookiecutter.friendly_name }}*!

No contribution is too small -- whether it be a typo fix, documentation improvements, or a new feature: all are welcome!

This document provides guidelines and instructions for contributing. It is supposed to clarify expectations and help you get started. It is not supposed to be a barrier, so don't be afraid to ask questions if something is unclear or to open a half-finished Pull Request (PR)!

## Development

To start developing *{{ cookiecutter.friendly_name }}*, follow these instructions to setup your development environment:

1. Create a *fork* (your own personal copy) of the *{{ cookiecutter.friendly_name }}* repository via https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.app_name }}/fork.

1. Clone the repository by replacing `<YOUR-USERNAME>` with your GitHub username:

   ```shell
   git clone https://github.com/<YOUR-USERNAME>/{{ cookiecutter.app_name }}.git
   cd {{ cookiecutter.app_name }}
   ```

1. Install uv (if not already installed):

   ```shell
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

   See https://docs.astral.sh/uv/getting-started/installation/ for additional installation methods.

1. Create a virtual environment and install dependencies (including development dependencies):

   ```shell
   uv sync --dev
   ```

1. Install [pre-commit](https://pre-commit.com/) hooks:

   ```shell
   uv run prek install
   ```

## Making Changes

1. Create a branch for your changes by replacing `<NEW-BRANCH>` with the name of your new branch (e.g., `improve-docs` if you're planning on submitting documentation improvements):

   ```shell
   git switch -c <NEW-BRANCH>
   ```

1. Make your changes following the coding standards (see below).

1. Ensure all tests pass:

   ```shell
   uv run pytest
   ```

1. Ensure all pre-commit hooks pass:

   ```shell
   uv run prek run --all-files
   ```

1. Update documentation if needed (in `README.md` and/or `docs/`).

1. Add tests for any new or changed functionality.

1. Add an entry to `CHANGELOG.md` under the `[Unreleased]` section.

## Coding Standards

### Code Formatting

*{{ cookiecutter.friendly_name }}* adheres to [the Black code style](https://black.readthedocs.io/en/stable/the_black_code_style/current_style.html) and uses [Ruff](https://docs.astral.sh/ruff/) for linting and formatting code. Make sure your code is formatted properly:

```shell
uv run prek run --all-files ruff-check ruff-format
```

### Typing

*{{ cookiecutter.friendly_name }}* uses type hints/annotations throughout, and uses a combination of [mypy](https://mypy.readthedocs.io/en/stable/), [Pyrefly](https://pyrefly.org/), [Pyright](https://microsoft.github.io/pyright/#/), [ty](https://docs.astral.sh/ty/) and [Zuban](https://zubanls.com/) to do type checking. Please add type annotations for all new code, and make sure that type checking succeeds:

```shell
uv run prek run --all-files mypy pyrefly-check pyright ty-check zuban-check
```

### Testing

*{{ cookiecutter.friendly_name }}* has a comprehensive test suite, which includes smoke tests, unit tests and integration tests, and uses [pytest](https://docs.pytest.org/en/stable/) to execute it:

```shell
uv run pytest
```

Tests are required for any new/changed functionality. Add/update tests in the `tests/` directory.

### Docstrings

*{{ cookiecutter.friendly_name }}* uses [Google Style Python Docstrings](https://www.sphinx-doc.org/en/master/usage/extensions/example_google.html) to document its API:

```python
def function_name(arg1: Type1, arg2: Type2) -> ReturnType:
    """Brief description of function.

    More detailed description if needed.

    Args:
        arg1: Description of arg1.
        arg2: Description of arg2.

    Returns:
        Description of return value.

    Raises:
        ValueError: When and why this is raised.
    """
```

Make sure you add or update docstrings for any API changes.

### CLI Reference

The CLI reference in `README.md` and `docs/cli.md` is generated from the actual `--help` output of *{{ cookiecutter.friendly_name }}* with [cog](https://cog.readthedocs.io/en/latest/). If you change the command-line interface, regenerate it:

```shell
uv run prek run --all-files cog
```

### Changelog

*{{ cookiecutter.friendly_name }}* follows the [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) format for its changelog:

```markdown
### Added

- Added `--flag` for cool functionality.
```

If your change is relevant to end-users, make sure to add an entry to `CHANGELOG.md`.

## Creating a Pull Request

Once you're happy with your change and all checks and tests pass (by following the steps above), you can [create a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork). Please make sure you include a good description of what your change does, and link it to any relevant issues or discussions.

When you create your pull request, *{{ cookiecutter.friendly_name }}*'s [CI](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.app_name }}/actions) will run the same checks and tests described earlier. If they fail, please (attempt to) fix them, as it is unlikely your pull request will be reviewed until then. If you've tried everything and still can't fix a failing check or test, bump the pull request with a short note saying as much, and someone may be able to offer assistance.

### Code Review

After the checks and tests in your pull request pass, someone will review your pull request and provide feedback. Once you've addressed the review feedback, bump the pull request with a short note saying as much to signal that you're done.

### Merging

When your pull request is approved, it will be merged into the `main` branch. Your change will only be available to users the next time *{{ cookiecutter.friendly_name }}* is released.
