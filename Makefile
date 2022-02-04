install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-install-reinforced:
	python3 -m pip install --user --force-reinstall dist/*.whl

lint:
	poetry run flake8 gendiff

gendiff:
	poetry run gendiff -h


.PHONY: test
test:
	poetry run pytest


test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

gendiff1:
	poetry run gendiff tests/fixtures/file1.json tests/fixtures/file2.json 	

gendiff2:
	poetry run gendiff tests/fixtures/file1.yaml tests/fixtures/file2.yaml 	

gendiff3:
	poetry run gendiff tests/fixtures/file_tree1.json tests/fixtures/file_tree2.json	

gendiff4:
	poetry run gendiff tests/fixtures/file_tree1.yaml tests/fixtures/file_tree2.yaml

	
