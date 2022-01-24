#!/usr/bin/env python3


def generate_diff(file1, file2):
    result = '{\n'
    all_keys = sorted(list(file1.keys() | file2.keys()))
    two_keys = file1.keys() & file2.keys()
    deleted_keys = file1.keys() - file2.keys()
    added_keys = file2.keys() - file1.keys()
    for key in all_keys:
        if key in two_keys:
            if file1[key] == file2[key]:
                result += '    {}: {}\n'.format(key, file1[key])
            else:
                result += '  - {}: {}\n'.format(key, file1[key])
                result += '  + {}: {}\n'.format(key, file2[key])
        elif key in deleted_keys:
            result += '  - {}: {}\n'.format(key, file1[key])
        elif key in added_keys:
            result += '  + {}: {}\n'.format(key, file2[key])

    result += '}'
    return result
