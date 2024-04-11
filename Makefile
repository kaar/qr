init:
	poetry install

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
	rm -rf .venv
.PHONY: clean
