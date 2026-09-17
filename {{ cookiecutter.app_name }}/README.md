<!-- start docs-include-index -->

# {{ cookiecutter.friendly_name }}

[![PyPI](https://img.shields.io/pypi/v/{{ cookiecutter.app_name }})](https://img.shields.io/pypi/v/{{ cookiecutter.app_name }})
[![Supported Python Versions](https://img.shields.io/pypi/pyversions/{{ cookiecutter.app_name }})](https://pypi.org/project/{{ cookiecutter.app_name }}/)
[![CI](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.app_name }}/actions/workflows/ci.yml/badge.svg)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.app_name }}/actions/workflows/ci.yml)
[![Test](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.app_name }}/actions/workflows/test.yml/badge.svg)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.app_name }}/actions/workflows/test.yml)
[![Documentation Status](https://readthedocs.org/projects/{{ cookiecutter.app_name }}/badge/?version=latest)](https://{{ cookiecutter.app_name }}.readthedocs.io/en/latest/?badge=latest)

<!-- [![OpenSSF Best Practices](https://www.bestpractices.dev/projects/<PROJECT-NUMBER>/badge)](https://www.bestpractices.dev/projects/<PROJECT-NUMBER>) -->

{{ cookiecutter.short_description }}

<!-- end docs-include-index -->

## Installation

<!-- start docs-include-installation -->

*{{ cookiecutter.friendly_name }}* is available on [PyPI](https://pypi.org/project/{{ cookiecutter.app_name }}/). Install with [uv](https://docs.astral.sh/uv/) or your package manager of choice:

```shell
uv tool install {{ cookiecutter.app_name }}
```

<!-- end docs-include-installation -->

## Documentation

Check out the [*{{ cookiecutter.friendly_name }}* documentation](https://{{ cookiecutter.app_name }}.readthedocs.io/en/stable/) for the [User's Guide](https://{{ cookiecutter.app_name }}.readthedocs.io/en/stable/usage.html) and [CLI Reference](https://{{ cookiecutter.app_name }}.readthedocs.io/en/stable/cli.html).

## Usage

<!-- start docs-include-usage -->

Running `{{ cookiecutter.app_name }} --help` or `python -m {{ cookiecutter.package_name }} --help` shows a list of all of the available options and arguments:

<!-- [[[cog
import cog
from click.testing import CliRunner
from {{ cookiecutter.package_name }} import cli
result = CliRunner().invoke(cli.cli, ["--help"], terminal_width=88)
output = result.output.replace("Usage: cli", "Usage: {{ cookiecutter.app_name }}")
help_text = "\n".join(line.rstrip() for line in output.splitlines()).rstrip()
cog.outl(f"\n```shell\n{{ cookiecutter.app_name }} --help\n{help_text}\n```\n")
]]] -->
<!-- [[[end]]] -->

<!-- end docs-include-usage -->
