.PHONY: superuser isntall migrations migrate update shell
superuser:
	poetry run python -m marketplace.manage createsuperuser

install:
	poetry install

migrations:
	poetry run python -m marketplace.manage makemigrations

migrate:
	poetry run python -m marketplace.manage migrate

run-server:
	poetry run python -m marketplace.manage runserver

lint:
	poetry run pylint marketplace
	poetry run black --check marketplace
	poetry run isort --check marketplace

format:
	poetry run black marketplace
	poetry run isort marketplace

update: install migrate;

shell:
	poetry run python -m marketplace.manage shell
