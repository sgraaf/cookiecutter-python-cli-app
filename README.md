# cookiecutter-python-cli-app

[![Supported Python Versions](https://img.shields.io/badge/python-3.11%20%7C%203.12%20%7C%203.13%20%7C%203.14%20%7C%203.15-blue)](https://github.com/sgraaf/cookiecutter-python-cli-app)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![prek](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/j178/prek/master/docs/assets/badge-v0.json)](https://github.com/j178/prek)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![ty](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ty/main/assets/badge/v0.json)](https://github.com/astral-sh/ty)

A [cookiecutter](https://cookiecutter.readthedocs.io/) template for creating a new Python command-line application with [Click](https://click.palletsprojects.com/).

See https://github.com/sgraaf/cookiecutter-python-cli-app-demo for a demo of this template.

## Usage

```shell
cookiecutter gh:sgraaf/cookiecutter-python-cli-app
```

## Features

- Beautiful and powerful command-line interfaces with [Click](https://click.palletsprojects.com/), optionally enhanced with [rich-click](https://ewels.github.io/rich-click/)
- Linting with autofix (i.e. removing unused imports, detecting code smells and Python syntax upgrades) with [Ruff](https://docs.astral.sh/ruff/)
- Code formatting with [Ruff](https://docs.astral.sh/ruff/), [Mdformat](https://mdformat.readthedocs.io/en/stable/) and [Prettier](https://prettier.io/)
- Static type-checking [ty](https://docs.astral.sh/ty/) for the entire project, and with [mypy](http://www.mypy-lang.org/), [Pyrefly](https://pyrefly.org/), [Pyright](https://microsoft.github.io/pyright/#/) and [Zuban](https://zubanls.com/) for the public API (i.e., the test suite)
- Checks and fixes before every commit with [prek](https://prek.j178.dev/)
- Testing with [pytest](https://docs.pytest.org/en/stable/)
- Extremely fast Python package and project management with [uv](https://docs.astral.sh/uv/)
- Continuous Integration with [GitHub Actions](https://github.com/features/actions)
- Automated version updates for GitHub Actions with [Dependabot](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/keeping-your-actions-up-to-date-with-dependabot)
- Documentation with [Sphinx](https://www.sphinx-doc.org/en/master/), [MyST](https://myst-parser.readthedocs.io/en/latest/) and [Read the Docs](https://readthedocs.org/), using the [Furo](https://pradyunsg.me/furo/) theme, with an always up-to-date CLI reference courtesy of [cog](https://cog.readthedocs.io/en/latest/)
- A choice of 15 licenses, and optional Git repository initialization
- Automated release builds and uploads to [PyPI](https://pypi.org/)

This template supports Python 3.11, 3.12, 3.13, 3.14 and 3.15.
