from gendiff.formatters import format_stylish, format_plain, format_json


FORMAT_TYPES = {
    'stylish': format_stylish.to_slylish,
    'plain': format_plain.to_plain,
    'json': format_json.to_json,
}


def select_formatter(diff, style='stylish'):
    formatter = FORMAT_TYPES.get(style)
    return formatter(diff)
