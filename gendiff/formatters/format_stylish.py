"""This is string formatter."""
from gendiff.constants import (
    ADDED,
    CHANGED,
    CONDITION,
    DELETED,
    NESTED,
    UNCHANGED,
    VALUE,
)

FORMAT_STRING = '{0}{1}{2}: {3}\n'
OFFSETS = '    '


def get_stylish(diff_structure):
    """Convert format_dict to string format.
    Parameters:
        diff_structure(dict): dict of difference.
    Returns:
        result string.
    """
    tabs = ''
    return '{{\n{0}}}'.format(''.join(_for_stylish(diff_structure, tabs)))


def _for_stylish(diff, tab):
    string = []
    for key in sorted(diff.keys()):
        condition = UNCHANGED
        if isinstance(diff[key], dict):
            condition = diff[key].get(CONDITION)
        if condition == CHANGED:
            string.append(FORMAT_STRING.format(
                tab,
                get_key_prefix(DELETED),
                key,
                format_value(diff[key][VALUE][DELETED], tab + OFFSETS),
            ))
            string.append(FORMAT_STRING.format(
                tab,
                get_key_prefix(ADDED),
                key,
                format_value(diff[key][VALUE][ADDED], tab + OFFSETS),
            ))
        elif condition in (ADDED, DELETED, NESTED, UNCHANGED, None):
            string.append(FORMAT_STRING.format(
                tab,
                get_key_prefix(condition),
                key,
                format_value(diff[key], tab + OFFSETS),
            ))
    return string


def format_value(data_items, tab):
    if isinstance(data_items, dict) and VALUE in data_items:
        return format_value(data_items[VALUE], tab)
    elif isinstance(data_items, dict):
        return '{{\n{0}{1}}}'.format(
            ''.join(_for_stylish(data_items, tab)),
            tab,
        )
    return converting_stylish(data_items)


def get_key_prefix(value):
    if value == DELETED:
        return '  - '
    elif value == ADDED:
        return '  + '
    return '    '


def converting_stylish(value):
    if isinstance(value, bool):
        return (str(value)).lower()
    elif value is None:
        return 'null'
    return value
