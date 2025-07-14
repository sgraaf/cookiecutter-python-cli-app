"""Main CLI for {{ cookiecutter.app_name }}."""

from importlib import metadata

import {%- if cookiecutter.use_rich %} rich_click as {%- endif %} click


@click.command(
    context_settings={"help_option_names": ["-h", "--help"], "show_default": True}
)
{%- if cookiecutter.use_rich %}
@click.rich_config(
    help_config=click.RichHelpConfiguration(
        width=88,
        show_arguments=True,
        use_rich_markup=True,
    ),
)
{%- endif %}
@click.argument("input_", metavar="INPUT")
@click.option(
    "-r",
    "--reverse",
    is_flag=True,
    help="Reverse the input.",
)
@click.version_option(metadata.version("{{ cookiecutter.package_name }}"), "-v", "--version")
def cli(input_: str, *, reverse: bool = False) -> None:
    """Repeat the input.

    {{ cookiecutter.short_description }}
    """
    click.echo(input_ if not reverse else input_[::-1])
