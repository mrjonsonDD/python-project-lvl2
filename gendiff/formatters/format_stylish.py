import json
import itertools
from gendiff.constants import (
    ADDED,
    UPDATED,
    REMOVED,
    UNCHANGED,
    NESTED,
    TYPE,
    VALUE,
    OLD_VAL,
    NEW_VAL,
    CHILDREN
)


DEFAULT_INDENT = 4
TYPES_TO_INDENTS = {
    'added': '  + ',
    'removed': '  - ',
    'unchanged': '    ',
    'nested': '    '}


# flake8: noqa: C901
def to_slylish(diff):
    level = 0
    result = ''
    if diff:
        lines = [stringify_node(elem, level) for elem in diff.items()]
        result = '{\n' + '\n'.join(lines) + '\n}'
    return result


def stringify_node(item, level=0):
    indent = get_indent(level)
    key, item_value = item
    item_type = item_value.get(TYPE)

    if item_type == NESTED:
        children = item_value.get(CHILDREN)   
        new_lines = [
            stringify_node(child, level + 1) 
            for child in list(children.items())
        ]
        child_str = '{\n' + '\n'.join(new_lines) + '\n'+ indent + TYPES_TO_INDENTS['nested'] + '}'
        item_str = f"{indent}    {key}: {child_str} "
        return item_str

    if item_type == UPDATED:
        value1 = item_value.get(OLD_VAL)
        value2 = item_value.get(NEW_VAL)
        val1 = stringify_value(value1, level + 1)
        val2 = stringify_value(value2, level + 1)
        res_str1 = f"{indent}{TYPES_TO_INDENTS['removed']}{key}: {val1}"
        res_str2 = f"{indent}{TYPES_TO_INDENTS['added']}{key}: {val2}"
        item_str = res_str1 + '\n' + res_str2
        return item_str

    value = item_value.get(VALUE)
    val = stringify_value(value, level + 1)

    if item_type == UNCHANGED:
        return f"{indent}{TYPES_TO_INDENTS['unchanged']}{key}: {val}"

    if item_type == REMOVED:
        item_str = f"{indent}{TYPES_TO_INDENTS['removed']}{key}: {val}"
        return item_str

    if item_type == ADDED:
        item_str = f"{indent}{TYPES_TO_INDENTS['added']}{key}: {val}"
        return item_str    


def stringify_value(value, level):
    if not isinstance(value, dict):
        if value is None or isinstance(value, bool):
            return json.dumps(value)
        else:
            return value
    indent = get_indent(level)
    lines = []
    for key, val in value.items():
        lines.append(f'{indent}    {key}: {stringify_value(val, level+1)}')
    result = itertools.chain("{", lines, [indent +"}"])
    return '\n'.join(result)


def get_indent(level):
    indent = level * DEFAULT_INDENT * ' '
    return indent
