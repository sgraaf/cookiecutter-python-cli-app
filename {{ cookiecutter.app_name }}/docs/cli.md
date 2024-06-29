# CLI Reference

This page lists the `--help` for `{{ cookiecutter.app_name }}`.

## {{ cookiecutter.app_name }}

Running `{{ cookiecutter.app_name }} --help` or `python -m {{ cookiecutter.package_name }} --help` shows a list of all of the available options and arguments:

<!-- [[[cog
import cog
from {{ cookiecutter.package_name }} import cli
from click.testing import CliRunner
result = CliRunner().invoke(cli.cli, ["--help"], terminal_width=88)
help = result.output.replace("Usage: cli", "Usage: {{ cookiecutter.app_name }}")
cog.outl(f"\n```sh\n{{ cookiecutter.app_name }} --help\n{help.rstrip()}\n```\n")
]]] -->
<!-- [[[end]]] -->
