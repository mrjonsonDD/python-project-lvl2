import pytest
#import os
from gendiff.generate import generate_diff



@pytest.mark.parametrize(
    "file1, file2, expected_file, format",
    [
        ('tests/fixtures/file1.json', 'tests/fixtures/file2.json', 'tests/fixtures/result_simple.txt', 'json'),
        ('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml', 'tests/fixtures/result_simple.txt', 'json'),
        ('tests/fixtures/file_tree1.json', 'tests/fixtures/file_tree2.json', 'tests/fixtures/result_plain.txt', 'plain'),
        ('tests/fixtures/file_tree1.yaml', 'tests/fixtures/file_tree2.yaml', 'tests/fixtures/result_plain.txt', 'plain'),
        ('tests/fixtures/file_tree1.json', 'tests/fixtures/file_tree2.json', 'tests/fixtures/result_stylish.txt', 'stylish'),
        ('tests/fixtures/file_tree1.json', 'tests/fixtures/file_tree2.json', 'tests/fixtures/result_json.txt', 'json'),
        ('tests/fixtures/file_tree1.yaml', 'tests/fixtures/file_tree2.yaml', 'tests/fixtures/result_json.txt', 'json'),
    ]
)


def test_generate_diff(file1, file2, expected_file, format):
    with open(expected_file, 'r') as file:
        expected_data = file.read()

    assert generate_diff(file1, file2, format) == expected_data
