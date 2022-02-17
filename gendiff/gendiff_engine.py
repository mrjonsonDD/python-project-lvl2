"""This is the difference logic."""
from gendiff.formatters.format_json import get_json
from gendiff.formatters.format_plain import get_plain
from gendiff.formatters.format_stylish import get_stylish
from gendiff.parser_file import parse_file
from gendiff.diff_tree import build_diff_tree
from gendiff.constants import (
    JSON,
    PLAIN,
    STYLISH,
)


def generate_diff(file_path1, file_path2, formatter_name=STYLISH):
    """Get difference two file.
    Args:
        file_path1 (string): Path to the first file.
        file_path2 (string): Path to the second file.
        formatter_name (string): default = 'stylish'
    Returns:
        basestring: difference.
    """
    content_one = parse_file(file_path1)
    content_two = parse_file(file_path2)
    return select_formatter(formatter_name)(
        build_diff_tree(content_one, content_two),
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
