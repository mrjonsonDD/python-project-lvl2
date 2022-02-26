import pytest

from gendiff.parser_file import prepare_file


@pytest.mark.parametrize(
    'file_path',
    [
        ('tests/fixtures/wrong/wrong.ttt'),
        ('tests/fixtures/wrong/wrong.yml'),
        ('tests/fixtures/wrong/wrong.json'),
        ('file_not_exists'),
    ],
)
def test_wrong_file(file_path):
    with pytest.raises(Exception):
        assert prepare_file(file_path)
