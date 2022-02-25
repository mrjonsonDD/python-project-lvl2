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
	poetry run gendiff 

test:
	poetry run pytest -vv

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml tests/
