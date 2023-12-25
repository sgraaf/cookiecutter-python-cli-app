"""Main CLI for {{ cookiecutter.app_name }}."""
import {%- if cookiecutter.use_rich %} rich_click as {%- endif %} click

from . import __version__


@click.group()
{%- if cookiecutter.use_rich %}
@click.rich_config(
    help_config=click.RichHelpConfiguration(use_rich_markup=True, width=88)
)
{%- endif %}
@click.version_option(__version__)
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
