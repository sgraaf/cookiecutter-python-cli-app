<!-- start docs-include-index -->

# {{ cookiecutter.friendly_name }}

[![PyPI](https://img.shields.io/pypi/v/{{ cookiecutter.app_name }})](https://img.shields.io/pypi/v/{{ cookiecutter.app_name }})
[![Supported Python Versions](https://img.shields.io/pypi/pyversions/{{ cookiecutter.app_name }})](https://pypi.org/project/{{ cookiecutter.app_name }}/)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/{{ cookiecutter.github_username }}/{{ cookiecutter.app_name }}/main.svg)](https://results.pre-commit.ci/latest/github/{{ cookiecutter.github_username }}/{{ cookiecutter.app_name }}/main)
[![Test](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.app_name }}/actions/workflows/test.yml/badge.svg)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.app_name }}/actions/workflows/test.yml)
[![Documentation Status](https://readthedocs.org/projects/{{ cookiecutter.app_name }}/badge/?version=latest)](https://{{ cookiecutter.app_name }}.readthedocs.io/en/latest/?badge=latest)
[![PyPI - License](https://img.shields.io/pypi/l/{{ cookiecutter.app_name }})](https://img.shields.io/pypi/l/{{ cookiecutter.app_name }})

{{ cookiecutter.short_description }}

<!-- end docs-include-index -->

## Installation

<!-- start docs-include-installation -->

{{ cookiecutter.friendly_name }} is available on [PyPI](https://pypi.org/project/{{ cookiecutter.app_name }}/). Install with [pipx](https://pypa.github.io/pipx/) or your package manager of choice:

```sh
pipx install {{ cookiecutter.app_name }}
```

<!-- end docs-include-installation -->

## Documentation

Check out the [{{ cookiecutter.friendly_name }} documentation](https://{{ cookiecutter.app_name }}.readthedocs.io/en/stable/) for the [User's Guide](https://{{ cookiecutter.app_name }}.readthedocs.io/en/stable/usage.html) and [CLI Reference](https://{{ cookiecutter.app_name }}.readthedocs.io/en/stable/cli.html).

## Usage

<!-- start docs-include-usage -->

Running `{{ cookiecutter.app_name }} --help` or `python -m {{ cookiecutter.package_name }} --help` shows a list of all of the available options and commands:

<!-- [[[cog
import cog
from {{ cookiecutter.package_name }} import cli
from click.testing import CliRunner
runner = CliRunner()
result = runner.invoke(cli.cli, ["--help"], terminal_width=88)
help = result.output.replace("Usage: cli", "Usage: {{ cookiecutter.app_name }}")
cog.outl(f"\n```sh\n{{ cookiecutter.app_name }} --help\n{help.rstrip()}\n```\n")
]]] -->
<!-- [[[end]]] -->

<!-- end docs-include-usage -->
