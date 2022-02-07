"""Test generate diff with difference formats."""
import pytest
from gendiff.constants import JSON, PLAIN, STYLISH
from gendiff.gendiff_engine import generate_diff


@pytest.mark.parametrize('path1, path2, formatter, path_to_result', [
    ('tests/fixtures/file1.json', 'tests/fixtures/file2.json',
     STYLISH, 'tests/fixtures/result_simple.txt'
    ),
    ('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml',
     STYLISH, 'tests/fixtures/result_simple.txt'
    ),
    ('tests/fixtures/file_tree1.json', 'tests/fixtures/file_tree2.json',
     STYLISH, 'tests/fixtures/result_stylish.txt'
    ),
    ('tests/fixtures/file_tree1.yaml', 'tests/fixtures/file_tree2.yaml',
     STYLISH, 'tests/fixtures/result_stylish.txt'
    ),
    ('tests/fixtures/file1.json', 'tests/fixtures/file2.json',
     PLAIN, 'tests/fixtures/result_simple_plain.txt'
    ),
    ('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml',
     PLAIN, 'tests/fixtures/result_simple_plain.txt'
    ),
    ('tests/fixtures/file_tree1.json', 'tests/fixtures/file_tree2.json',
     PLAIN, 'tests/fixtures/result_plain.txt'
    ),
    ('tests/fixtures/file_tree1.yaml', 'tests/fixtures/file_tree2.yaml',
     PLAIN, 'tests/fixtures/result_plain.txt'
    ),
    ('tests/fixtures/file_tree1.json', 'tests/fixtures/file_tree2.json',
     JSON, 'tests/fixtures/result_json.txt'
    ),
    ('tests/fixtures/file_tree1.yaml', 'tests/fixtures/file_tree2.yaml',
     JSON, 'tests/fixtures/result_json.txt'
    ),
])
def test_formatters(path1, path2, formatter, path_to_result):  # noqa: D103
    assert generate_diff(
        path1,
        path2,
        formatter,
    ) == open_result_file(path_to_result)


def open_result_file(path_to_result):  # noqa: D103
    with open(path_to_result) as file_result:
        result = file_result.read()
    return result
