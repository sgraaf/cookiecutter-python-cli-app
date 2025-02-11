"""Utility functions for testing {{ cookiecutter.app_name }}."""

import subprocess
from collections.abc import Sequence
from dataclasses import dataclass
from os import PathLike
from typing import Any, Union

# copied from `typeshed`
StrOrBytesPath = Union[str, bytes, PathLike]
Command = Union[StrOrBytesPath, Sequence[StrOrBytesPath]]


@dataclass
class CommandResult:
    """Holds the captured result of an invoked command.

    Inspired by `click.testing.Result`.
    """

    exit_code: int
    stdout: str
    stderr: str


def run_command_in_shell(command: Command, **kwargs: Any) -> CommandResult:
    """Execute a command through the shell, capturing the exit code and output."""
    result = subprocess.run(  # noqa: S602
        command,
        shell=True,
        capture_output=True,
        check=False,
        **kwargs,
    )
    return CommandResult(
        result.returncode,
        result.stdout.decode().replace("\r\n", "\n"),
        result.stderr.decode().replace("\r\n", "\n"),
    )
