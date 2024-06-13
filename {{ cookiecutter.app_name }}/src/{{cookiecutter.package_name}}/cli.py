"""Main CLI for {{ cookiecutter.app_name }}."""

import {%- if cookiecutter.use_rich %} rich_click as {%- endif %} click

from . import __version__

context_settings = {"help_option_names": ["-h", "--help"]}
{%- if cookiecutter.use_rich %}
help_config = click.RichHelpConfiguration(
    width=88,
    show_arguments=True,
    use_rich_markup=True,
)
{%- endif %}


@click.group(context_settings=context_settings)
{%- if cookiecutter.use_rich %}
@click.rich_config(help_config=help_config)
{%- endif %}
@click.version_option(__version__, "-v", "--version")
def cli() -> None:
    """{{ cookiecutter.short_description }}"""


@cli.command()
@click.argument("input_", metavar="INPUT")
@click.option(
    "-r",
    "--reverse",
    is_flag=True,
    help="Reverse the input.",
)
def repeat(input_: str, *, reverse: bool = False) -> None:
    """Repeat the input."""
    click.echo(input_ if not reverse else input_[::-1])
