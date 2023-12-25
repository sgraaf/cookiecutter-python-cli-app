import re

PACKAGE_PATTERN = re.compile(r"^[_a-zA-Z][_a-zA-Z0-9]+$")

package_name = "{{ cookiecutter.package_name }}"

if PACKAGE_PATTERN.match(package_name) is None:
    msg = f"Invalid package name: `{package_name}`. Please only use alphanumerics and underscores (_)."
    raise ValueError(msg)
