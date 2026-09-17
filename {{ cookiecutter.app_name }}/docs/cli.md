# CLI Reference

This page lists the `--help` for `{{ cookiecutter.app_name }}`.

## {{ cookiecutter.app_name }}

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
