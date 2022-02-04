import pytest
import os
from gendiff.generate import generate_diff



@pytest.mark.parametrize(
    'style, file_first, file_second, file_result',
    [
        ('json', 'tests/fixtures/file1.json', 'tests/fixtures/file2.json', 'tests/fixtures/result_simple.txt'),
        ('json', 'tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml', 'tests/fixtures/result_simple.txt'),
        ('plain', 'tests/fixtures/file_tree1.json', 'tests/fixtures/file_tree2.json', 'tests/fixtures/result_plain.txt'),
        ('plain', 'tests/fixtures/file_tree1.yaml', 'tests/fixtures/file_tree2.yaml', 'tests/fixtures/result_plain.txt'),
        ('stylish', 'tests/fixtures/file_tree1.json', 'tests/fixtures/file_tree2.json', 'tests/fixtures/result_stylish.txt'),
        ('json', 'tests/fixtures/file_tree1.json', 'tests/fixtures/file_tree2.json', 'tests/fixtures/result_json.txt'),
        ('json', 'tests/fixtures/file_tree1.yaml', 'tests/fixtures/file_tree2.yaml', 'tests/fixtures/result_json.txt'),
    ],
)


def test_generate_diff(style, file_first, file_second, file_result):
    with open(os.path.abspath(file_result)) as f:
        result = f.read()
    assert generate_diff(file_first, file_second, style) == result
