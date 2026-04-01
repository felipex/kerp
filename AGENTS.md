# AGENTS.md

Instructions for agentic coding agents working in this repository.

## Project Overview

kerp is a Django 6.0.3 ERP system (Python 3.14) for customer, sales, inventory, and
financial management. The architecture follows **Pragmatic DDD with a Service Layer**.
Documentation and comments are written in **Brazilian Portuguese**. Domain/field names
use English.

Tech stack: Django 6.x, HTMX, Tailwind CSS + DaisyUI, Alpine.js, PostgreSQL (prod) /
SQLite3 (dev/test), Celery + Redis, DRF + drf-spectacular, django-unfold.

Apps: `users` (custom User model), `core` (BaseModel abstract), `crm` (Customer, Contact).
`AUTH_USER_MODEL = 'users.User'`. Locale: `pt-br`, timezone: `America/Fortaleza`.

## Build / Run / Test Commands

```bash
# Install dependencies (inside .venv)
pip install -r requirements.txt

# Run dev server
python manage.py runserver

# Migrations
python manage.py makemigrations
python manage.py migrate

# Run all tests (set DJANGO_SETTINGS_MODULE if no pytest.ini exists)
DJANGO_SETTINGS_MODULE=kerp.settings pytest

# Run a single test file
DJANGO_SETTINGS_MODULE=kerp.settings pytest crm/tests.py

# Run a single test class
DJANGO_SETTINGS_MODULE=kerp.settings pytest crm/tests.py::TestClassName

# Run a single test method
DJANGO_SETTINGS_MODULE=kerp.settings pytest crm/tests.py::TestClassName::test_method

# Run tests by keyword
DJANGO_SETTINGS_MODULE=kerp.settings pytest -k "keyword"

# Verbose + coverage
DJANGO_SETTINGS_MODULE=kerp.settings pytest -v --cov
```

There is currently **no lint, format, or typecheck command configured**. When adding
tooling, prefer `ruff` for linting/formatting and `mypy` for type checking. Add a
`pyproject.toml` with `[tool.pytest.ini_options]` so `DJANGO_SETTINGS_MODULE` does not
need to be passed manually.

## Code Style Guidelines

### Imports
- Order: standard library, third-party (Django, external libs), local project imports.
- One blank line between each group.
- Use absolute imports. Avoid `from . import` except in `__init__.py` re-exports.
- Example ordering in models: `import uuid`, then `from django.conf import settings`
  / `from django.db import models` / `from django.utils import timezone`.

### Formatting & Naming
- 4-space indentation.
- Single quotes for strings in settings and code; double quotes for docstrings and
  `help_text`.
- Files: `snake_case.py`. Classes: `PascalCase`. Variables/methods: `snake_case`.
- Constants: `UPPER_SNAKE_CASE`.

### Django Models

All domain models extend `core.models.BaseModel` (abstract). BaseModel provides:
`id` (UUID7 PK), `created_at`, `updated_at`, `deleted_at`, `owner` (FK to User), and
soft-delete methods. Do not redefine these fields on subclasses.

Every model must follow this pattern:

```python
import uuid

from django.conf import settings
from django.db import models
from django.utils import timezone

from core.models import BaseModel


class Example(BaseModel):
    """Docstring in Portuguese describing the entity."""

    # ... domain fields only (no id/owner/timestamps — inherited from BaseModel) ...

    class Meta:
        ordering = ['field']
        verbose_name = 'Example'
        verbose_name_plural = 'Examples'

    def __str__(self):
        return self.display_name
```

Key rules:
- UUID7 primary key (`uuid.uuid7`) — inherited from BaseModel.
- `owner` ForeignKey with `on_delete=models.PROTECT` and `related_name='owned_%(class)s'`
  — inherited from BaseModel.
- Soft delete via `deleted_at`. Override `delete()` and add `restore()` on BaseModel.
- Use `timezone.now()` — import from `django.utils`.
- Always use `related_name` on ForeignKey/ManyToMany fields.
- Prefer `on_delete=models.PROTECT` over CASCADE for business entities.
- Property `is_deleted` returns `deleted_at is not None`.

### Project Structure
- Django apps live at the project root (e.g., `crm/`, not `apps/crm/`).
- Models may use a sub-package: `app/models/__init__.py` (re-exports) and
  `app/models/models.py` (definitions), as seen in `crm/`.
- Services go in `app/services.py` or `app/services/`.

### Architecture
- Use a **Service Layer** for business logic. Keep views thin.
- Domain logic belongs in services, not in views, serializers, or management commands.
- Use factories (factory-boy) for test data. Place in `app/factories.py`.

### Error Handling
- Raise domain-specific exceptions from the service layer.
- Catch exceptions in views and translate to user-facing messages via Django messages
  framework.
- Never swallow exceptions silently — log them.

### Templates & Frontend
- Use HTMX for dynamic interactions instead of custom JavaScript.
- Forms use django-crispy-forms with the Tailwind template pack.
- Use DaisyUI component classes in templates.

### Testing
- Use `pytest` with `pytest-django`.
- Place tests in `app/tests.py` or `app/tests/` directory.
- Use `factory-boy` factories for model creation.
- Name test files `test_*.py` and test functions `test_*`.
- Use `@pytest.mark.django_db` for tests that access the database.

### General Practices
- Do not commit secrets, `.env` files, or `db.sqlite3`.
- Do not add comments unless the code's intent is non-obvious.
- Keep functions and methods short and focused.
- Write docstrings in Portuguese for public classes and methods.
- Each app may have a `CONTEXT.md` with domain rules and relationships in Portuguese.
