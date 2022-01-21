import pytest
from gendiff.generate import generate_diff


@pytest.fixture
def extract_value(path):
    with open(path) as f:
        return f.read()




def test1(first_file, second_file):
    first_file = 'tests/fixtures/file1.json'
    second_file = 'tests/fixtures/file2.json'
    diff = generate_diff(first_file, second_file)
    differents_txt = extract_value('tests/fixtures/diff_json.txt')
    assert diff == differents_txt