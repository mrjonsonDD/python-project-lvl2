import json
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

# flake8: noqa: C901
def to_plain(diff, parent_key=''):
    result = ''
    items_diff = diff.items()
    if diff:
        lines = []
    for elem in items_diff:
        item_key, item_value = elem
        if item_value.get(TYPE) != UNCHANGED:
            lines.append(stringify_node(elem, parent_key))

        result = '\n'.join(lines)
    return result
            
    
def stringify_node(item, level):

    current_key, item_value = item

    item_type = item_value.get(TYPE)
    if level:
        key = f"{level}.{current_key}"
    else:
        key = current_key

    if item_type == NESTED:
        children = item_value.get(CHILDREN)
        items_children = to_plain(children, key)
        return items_children     
        
    if item_type == UPDATED:
        value1 = item_value.get(OLD_VAL)
        value2 = item_value.get(NEW_VAL)
        val1 = format_val(value1)
        val2 = format_val(value2)
        item_str = f"Property '{key}' was updated. From {val1} to {val2}"
        return item_str

    if item_type == REMOVED:
        item_str = f"Property '{key}' was removed"
        return item_str

    if item_type == ADDED:
        value = item_value.get(VALUE)
        val = format_val(value)
        item_str = f"Property '{key}' was added with value: {val}"
        return item_str


def format_val(value):
    """Function stringifies value if it is a dict"""
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        if value is None or isinstance(value, bool):
            return json.dumps(value)
        else:
            return value
