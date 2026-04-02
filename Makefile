.PHONY: run migrate shell test install clean

# Variáveis
PYTHON = uv run python
MANAGE = $(PYTHON) manage.py

run:
	uv run manage.py runserver

migrate:
	$(MANAGE) makemigrations
	$(MANAGE) migrate

shell:
	$(MANAGE) shell_plus  # Se usar o django-extensions, ou apenas shell

test:
	uv run pytest --reuse-db

install:
	uv sync

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -rf .pytest_cache
