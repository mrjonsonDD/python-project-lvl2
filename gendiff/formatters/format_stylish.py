from gendiff.constants import (
    ADDED,
    CHANGED,
    DELETED,
    NESTED,
    UNCHANGED
)

DEFAULT_INDENT = 4
STATUS_INDENT = 2
STATUSES = {
    ADDED: '+',
    DELETED: '-',
    UNCHANGED: ' ',
    NESTED: ' ',
}


def format_stylish(diff, depth=0):  # noqa: C901
    indent = depth * DEFAULT_INDENT * ' '
    next_depth = depth + 1
    res = []
    for key, value in sorted(diff.items()):
        if isinstance(value, list):
            status, *rest = value
            if status == CHANGED:
                res.append(generate_string(DELETED, key, rest[0], next_depth))
                res.append(generate_string(ADDED, key, rest[1], next_depth))
                continue
            res.append(generate_string(status, key, rest[0], next_depth))
            continue
        res.append(generate_string(UNCHANGED, key, value, next_depth))
    return '{\n' + '\n'.join(res) + '\n' + indent + '}'


def generate_string(status, key, value, depth):
    indent = (depth * DEFAULT_INDENT - STATUS_INDENT) * ' '
    if isinstance(value, dict):
        result = format_stylish(value, depth)
        return f'{indent}{STATUSES[status]} {key}: {result}'
    return f'{indent}{STATUSES[status]} {key}: {format_value(value)}'


def format_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return value
