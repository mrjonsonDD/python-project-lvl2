from gendiff.constants import (
    ADDED,
    UPDATED,
    REMOVED,
    UNCHANGED,
    DICT,
    TYPE,
    VALUE,
    OLD_VAL,
    NEW_VAL,
    CHILDREN
)

# flake8: noqa: C901
def to_plain(diff):

    def stringify(item, parent_key=''):
        current_key, item_value = item
        item_type = item_value.get(TYPE)
        if parent_key:
            key = f"{parent_key}.{current_key}"
        else:
            key = current_key

        if item_type == DICT:
            children = item_value.get(CHILDREN)
            new_lines = [stringify(child, key) 
                for child in list(children.items())
                if child[1].get(TYPE) != UNCHANGED]
            child_str = '\n'.join(new_lines)
            return child_str
        
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

    result = ''
    if diff:
        lines = [stringify(elem) 
            for elem in list(diff.items())
            if elem[1].get(TYPE) != UNCHANGED]
        result = '\n'.join(lines)
    return result


def format_val(value):
    """Function stringifies value if it is a dict"""
    replace_dict = {
        None: 'null',
        True: 'true',
        False: 'false'
    }
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        if value in replace_dict.keys() and type(value) is not int:
            return replace_dict[value]
        else:
            return value
