import pytest
from gendiff.parser import prepare_file
from gendiff.generate import generate_diff
from pathlib import Path


def test1(file1, file2):
    base_path = Path(__file__).parent
    file_path = (base_path / "../tests/fixtures/diff_file_text.txt").resolve()
    file1 = prepare_file('tests/fixtures/file1.json')
    file2 = prepare_file('tests/fixtures/file2.json')
    with open(file_path, 'r') as f:
        assert generate_diff(file1, file2) == f.read()
        assert type(generate_diff(file1, file2)) == str

def tast2(file1, file2):
    base_path = Path(__file__).parent
    file_path = (base_path / "../tests/fixtures/diff_file_text.txt").resolve()
    file1 = prepare_file('tests/fixtures/file1.yaml')
    file2 = prepare_file('tests/fixtures/file2.yaml')
    with open(file_path, 'r') as f:
        assert generate_diff(file1, file2) == f.read()
        assert type(generate_diff(file1, file2)) == str

