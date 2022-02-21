"""This is the difference logic."""
from gendiff.formatters.get_format import select_formatter
from gendiff.parser_file import parse_file
from gendiff.diff_tree import build_diff_tree
from gendiff.constants import (
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
