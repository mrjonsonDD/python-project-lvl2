"""This is the difference logic."""
from gendiff.formatters.format_json import get_json
from gendiff.formatters.format_plain import get_plain
from gendiff.formatters.format_stylish import get_stylish
from gendiff.parser_file import parse_file
from gendiff.constants import (  # noqa:WPS235
    ADDED,
    CHANGED,
    CONDITION,
    DELETED,
    JSON,
    NESTED,
    PLAIN,
    STYLISH,
    UNCHANGED,
    VALUE,
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
    return _select_formatter(formatter_name)(
        _gen_diff(content_one, content_two),
    )


def _gen_diff(first_dict, second_dict):  # noqa: C901, WPS231, WPS210, WPS221, E501
    diff_diff = {}
    shared_keys = (first_dict.keys() & second_dict.keys())
    deleted_keys = (first_dict.keys() - second_dict.keys())
    added_keys = (second_dict.keys() - first_dict.keys())
    for key in deleted_keys:
        diff_diff[key] = {CONDITION: DELETED, VALUE: first_dict[key]}
    for key2 in shared_keys:
        if first_dict.get(key2) == second_dict.get(key2):
            diff_diff[key2] = {CONDITION: UNCHANGED, VALUE: first_dict[key2]}
        elif isinstance(second_dict.get(key2), dict) and isinstance(first_dict.get(key2), dict):  # noqa:E501, WPS221
            diff_diff[key2] = {
                CONDITION: NESTED,
                VALUE: _gen_diff(first_dict[key2], second_dict[key2]),
            }
        else:
            diff_diff[key2] = {
                CONDITION: CHANGED,
                VALUE: {
                    DELETED: first_dict[key2],
                    ADDED: second_dict[key2],
                },
            }
    for key3 in added_keys:
        diff_diff[key3] = {CONDITION: ADDED, VALUE: second_dict[key3]}
    return diff_diff


def _select_formatter(format_name):
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
