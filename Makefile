.PHONY: install run test test-coverage lint format format-check lint-fix check check-fix build

install:
	uv sync --all-extras

link:
	uv tool install --from ./gendiff gendiff

run:
	uv run gendiff

test:
	uv run pytest -v

test-coverage:
	uv run pytest --cov=gendiff --cov-report xml --cov-report term-missing

# Линтинг (проверка без исправлений)
lint:
	uv run ruff check .

# Форматирование кода (автоисправление форматирования)
format:
	uv run ruff format .

# Проверка форматирования (без исправлений)
format-check:
	uv run ruff format --check .

# Линтинг с автоисправлением (исправит то, что может)
lint-fix:
	uv run ruff check --fix .

# Полная проверка (без исправлений)
check:
	make lint
	make test
	make format-check

# Полная проверка с автоисправлением
check-fix:
	make lint-fix
	make format
	make test

build:
	uv build