"""This is string formatter."""
from gendiff.constants import (
    ADDED,
    CHANGED,
    TYPE,
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
    return '{{\n{0}}}'.format(''.join(for_stylish(diff_structure, tabs)))


def for_stylish(diff, tab):
    str_list = []
    for key in sorted(diff.keys()):
        condition = UNCHANGED
        if isinstance(diff[key], dict):
            condition = diff[key].get(TYPE)
        if condition == CHANGED:
            str_list.append(FORMAT_STRING.format(
                tab,
                get_key_prefix(DELETED),
                key,
                format_value(diff[key][VALUE][DELETED], tab + OFFSETS),
            ))
            str_list.append(FORMAT_STRING.format(
                tab,
                get_key_prefix(ADDED),
                key,
                format_value(diff[key][VALUE][ADDED], tab + OFFSETS),
            ))
        elif condition in (ADDED, DELETED, NESTED, UNCHANGED, None):
            str_list.append(FORMAT_STRING.format(
                tab,
                get_key_prefix(condition),
                key,
                format_value(diff[key], tab + OFFSETS),
            ))
    return str_list


def format_value(data_items, tab):
    if isinstance(data_items, dict) and VALUE in data_items:
        return format_value(data_items[VALUE], tab)
    elif isinstance(data_items, dict):
        return '{{\n{0}{1}}}'.format(
            ''.join(for_stylish(data_items, tab)),
            tab,
        )
    return converting_stylish(data_items)


def get_key_prefix(node_type_name):
    if node_type_name == DELETED:
        return '  - '
    elif node_type_name == ADDED:
        return '  + '
    return '    '


def converting_stylish(value):
    if isinstance(value, bool):
        return (str(value)).lower()
    elif value is None:
        return 'null'
    return value
