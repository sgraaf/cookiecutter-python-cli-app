import re

PACKAGE_PATTERN = re.compile(r"^[_a-zA-Z][_a-zA-Z0-9]+$")


def validate_package_name(package_name: str) -> None:
    if PACKAGE_PATTERN.match(package_name) is None:
        msg = f"Invalid package name: `{package_name}`. Please only use alphanumerics and underscores (_)."
        raise ValueError(msg)


def validate_description(description: str) -> None:
    if not description.endswith("."):
        msg = f"Invalid description: `{description}`. It should end with a single period (.)."
        raise ValueError(msg)


if __name__ == "__main__":
    validate_package_name("{{ cookiecutter.package_name }}")
    validate_description("{{ cookiecutter.short_description }}")
