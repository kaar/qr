.venv/pyvenv.cfg:
	poetry install

init: .venv/pyvenv.cfg
.PHONY: init

lint: init
	poetry run black --check ./
	poetry run ruff check ./
.PHONY: lint

format: init
	poetry run black ./
.PHONY: lint

test: init
	poetry run pytest --cov=qr --cov-report=term-missing

run: init
	poetry run python -m qr.qr

clean:
	poetry --rm
.PHONY: clean
