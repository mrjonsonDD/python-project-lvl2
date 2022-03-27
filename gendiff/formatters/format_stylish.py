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


REPLACER = '  '
SPACE_CNT = 1


# flake8: noqa: C901
def to_slylish(diff):
    result = ''
    if diff:
        lines = [stringify_node(elem, 0) for elem in diff.items()]
        result = '{\n' + '\n'.join(lines) + '\n}'
    return result


def stringify_node(item, depth):
    key, item_value = item
    item_type = item_value.get(TYPE)
    indent = get_indent(depth)['indent']
    space = get_indent(depth)['space']
    
    if item_type == NESTED:
        children = item_value.get(CHILDREN)   
        new_lines = [
            stringify_node(child, indent) 
            for child in list(children.items())
        ]
        child_str = '{\n' + '\n'.join(new_lines) + '\n' + space + '}'
        item_str = f"{REPLACER * (depth + 1)}  {key}: {child_str}"
        return item_str

    if item_type == UPDATED:
        value1 = item_value.get(OLD_VAL)
        value2 = item_value.get(NEW_VAL)
        val1 = stringify_value(value1, indent)
        val2 = stringify_value(value2, indent)
        res_str1 = f"{REPLACER * (depth + 1)}- {key}: {val1}"
        res_str2 = f"{REPLACER * (depth + 1)}+ {key}: {val2}"
        item_str = res_str1 + '\n' + res_str2
        return item_str

    value = item_value.get(VALUE)
    val = stringify_value(value, indent)

    if item_type == UNCHANGED:
        return f"{REPLACER * (depth + 1)}  {key}: {val}"

    if item_type == REMOVED:
        item_str = f"{REPLACER * (depth + 1)}- {key}: {val}"
        return item_str

    if item_type == ADDED:
        item_str = f"{REPLACER * (depth + 1)}+ {key}: {val}"
        return item_str    


def get_indent(depth):
    indent = depth + 2
    space = REPLACER * indent
    indent_str = REPLACER * depth
    current_indent = {
        'indent': indent,
        'space': space,
        'indent_str': indent_str
    }
    return current_indent


def stringify_value(value, depth):
    if not isinstance(value, dict):
        if value is None or isinstance(value, bool):
            return json.dumps(value)
        else:
            return value
    indent = get_indent(depth)['indent']
    space = get_indent(depth)['space']
    indent_str = get_indent(depth)['indent_str']
    lines = []
    for key, val in value.items():
        lines.append(f'{space}{key}: {stringify_value(val, indent)}')
    result = itertools.chain("{", lines, [indent_str + "}"])
    return '\n'.join(result)
