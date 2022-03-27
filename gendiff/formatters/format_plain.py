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
def to_plain(diff):
    result = ''
    items_diff = diff.items()
    if diff:
        result = get_value(items_diff, indent='')
    return result
    
    
def get_value(items, indent):
    lines = []
    for elem in items:
        item_key, item_value = elem
        if item_value.get(TYPE) != UNCHANGED:
            lines.append(stringify_value(elem, indent))
    result = '\n'.join(lines)
    return result
            
    
def stringify_value(item, parent_key=''):

    current_key, item_value = item

    item_type = item_value.get(TYPE)
    if parent_key:
        key = f"{parent_key}.{current_key}"
    else:
        key = current_key

    if item_type == NESTED:
        children = item_value.get(CHILDREN)
        items_children = children.items()
        return get_value(items_children, key)     
        
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
