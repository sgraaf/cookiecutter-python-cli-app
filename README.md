# cookiecutter-python-cli-app

[![Supported Python Versions](https://img.shields.io/badge/python-3.9%20|%203.10%20|%203.11%20|%203.12%20|%203.13-blue)](https://github.com/sgraaf/cookiecutter-python-cli-app)
[![Nox](https://img.shields.io/badge/%F0%9F%A6%8A-Nox-D85E00.svg)](https://github.com/wntrblm/nox)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

A [cookiecutter](https://cookiecutter.readthedocs.io/) template for creating a new Python command-line application with [Click](https://click.palletsprojects.com/).

See https://github.com/sgraaf/cookiecutter-python-cli-app-demo for a demo of this template.

## Usage

```sh
cookiecutter gh:sgraaf/cookiecutter-python-cli-app
```

## Features

<!-- TODO: mention optional use of rich, choice of licenses, git and venv initialization -->

-   Beautiful and powerful command-line interfaces with [Click](https://click.palletsprojects.com/)
-   Linting with autofix (i.e. removing unused imports, formatting and Python syntax upgrades) with [ruff](https://beta.ruff.rs/docs/)
-   Code formatting with [ruff](https://beta.ruff.rs/docs/) and [Prettier](https://prettier.io/)
-   Static type-checking with [mypy](http://www.mypy-lang.org/)
-   Checks and fixes before every commit with [pre-commit](https://pre-commit.com/)
-   Testing with [pytest](https://docs.pytest.org/en/stable/index.html)
-   Project automation with [Nox](https://nox.thea.codes/en/stable/)
-   Extremely fast Python package and project management with [uv](https://docs.astral.sh/uv/)
-   Continuous Integration with [GitHub Actions](https://github.com/features/actions) and [pre-commit.ci](https://pre-commit.ci/)
-   Automated version updates for GitHub Actions with [Dependabot](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/keeping-your-actions-up-to-date-with-dependabot)
-   Documentation with [Sphinx](https://www.sphinx-doc.org/en/master/), [MyST](https://myst-parser.readthedocs.io/en/latest/), and [Read the Docs](https://readthedocs.org/) using the [Furo](https://pradyunsg.me/furo/) theme
-   Automated release builds and uploads to [PyPI](https://pypi.org/)

This template supports Python 3.9, 3.10, 3.11, 3.12 and 3.13.
