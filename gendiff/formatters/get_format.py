from gendiff import formatters


FORMAT_TYPES = {
    'stylish': formatters.stylish,
    'plain': formatters.plain,
    'json': formatters.json,
}


def get_format(diff, style='stylish'):
    formatter = FORMAT_TYPES.get(style)
    return formatter(diff)
