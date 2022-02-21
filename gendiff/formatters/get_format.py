from gendiff.formatters.format_json import get_json
from gendiff.formatters.format_plain import get_plain
from gendiff.formatters.format_stylish import get_stylish
from gendiff.constants import (
    JSON,
    PLAIN,
    STYLISH,
)


def select_formatter(format_name):
    """Select formatter for output format.
    Returns:
        output format
    """
    formatters = {
        STYLISH: get_stylish,
        PLAIN: get_plain,
        JSON: get_json,
    }
    return formatters[format_name]
