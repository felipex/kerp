# kerp

A Django 6.0 ERP system for customer, sales, inventory, and financial management.

## Tech Stack

- **Backend**: Django 6.0.3, Python 3.14
- **Database**: PostgreSQL (production), SQLite3 (development/testing)
- **Frontend**: HTMX, Tailwind CSS + DaisyUI, Alpine.js
- **APIs**: Django REST Framework + drf-spectacular
- **Tasks**: Celery + Redis
- **Admin**: django-unfold
- **Package Management**: uv

## Quick Start

### Prerequisites

- Python 3.14+
- uv package manager

### Installation

```bash
make install
```

### Run Development Server

```bash
make run
```

The server will be available at `http://localhost:8000`

### Database Setup

```bash
make migrate
```

### Run Tests

```bash
make test
```

## Project Structure

- `kerp/` — Main Django project settings
- `users/` — Custom User model and authentication
- `core/` — BaseModel abstract for all domain models
- `crm/` — Customer Relationship Management (customers, contacts)
- `templates/` — HTML templates with HTMX
- `docs/` — Additional documentation

## Configuration

Environment variables are managed via `.env` (not committed). Create a `.env` file in the project root:

```bash
DJANGO_SETTINGS_MODULE=kerp.settings
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///db.sqlite3
CELERY_BROKER_URL=redis://localhost:6379
```

## Development

### Available Commands

```bash
make run       # Run development server
make migrate   # Create and apply migrations
make test      # Run tests with pytest
make install   # Sync dependencies
make clean     # Remove cache files
make shell     # Open Django shell
```

### Code Style

- 4-space indentation
- `snake_case` for files and variables
- `PascalCase` for classes
- Portuguese docstrings and comments for domain logic
- Single quotes for strings, double quotes for docstrings
- Absolute imports (avoid relative imports outside `__init__.py`)

## Architecture

- **Pragmatic DDD with Service Layer**: Business logic in services, thin views
- **Soft deletes**: Models use `deleted_at` field
- **Factory pattern**: Use factory-boy for test data
- **UUID7 primary keys**: All models inherit from `BaseModel`
- **Always use `related_name`** on ForeignKey/ManyToMany fields

## Testing

Run tests with pytest:

```bash
DJANGO_SETTINGS_MODULE=kerp.settings pytest
```

Or use the Makefile:

```bash
make test
```

For test coverage:

```bash
DJANGO_SETTINGS_MODULE=kerp.settings pytest --cov
```

## Deployment

### Docker (Recommended)

```bash
docker build -t kerp .
docker run -p 8000:8000 kerp
```

### Production Setup

1. Set `DEBUG=False` in production
2. Configure PostgreSQL as the database
3. Run migrations: `python manage.py migrate`
4. Collect static files: `python manage.py collectstatic`
5. Use a production WSGI server (Gunicorn, uWSGI)
6. Configure Redis for Celery task queue
7. Run Celery worker: `celery -A kerp worker -l info`

### Environment Variables for Production

```bash
DEBUG=False
SECRET_KEY=generate-a-strong-key
ALLOWED_HOSTS=yourdomain.com
DATABASE_URL=postgresql://user:password@host:5432/kerp
CELERY_BROKER_URL=redis://redis-host:6379
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

## API Documentation

The API uses Django REST Framework with drf-spectacular for OpenAPI schema generation.

Access the interactive API documentation at:
- Swagger UI: `http://localhost:8000/api/schema/swagger-ui/`
- ReDoc: `http://localhost:8000/api/schema/redoc/`
- OpenAPI Schema: `http://localhost:8000/api/schema/`

## Troubleshooting

### Migration Issues

If migrations fail:

```bash
python manage.py makemigrations
python manage.py migrate --plan  # Preview migrations
python manage.py migrate
```

### Database Issues

Reset the database (development only):

```bash
rm db.sqlite3
python manage.py migrate
```

### Celery Issues

Ensure Redis is running:

```bash
redis-server
```

Check Celery worker logs:

```bash
celery -A kerp worker -l debug
```

## Contributing

### Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/your-username/kerp.git`
3. Create a virtual environment and install dependencies:
   ```bash
   make install
   ```
4. Create a feature branch: `git checkout -b feature/your-feature-name`

### Code Review Process

1. Ensure all tests pass: `make test`
2. Ensure code follows style guidelines (see Code Style section)
3. Write clear commit messages (see Commit Conventions below)
4. Submit a pull request with a detailed description
5. Address review feedback
6. A maintainer will merge once approved

### Commit Message Conventions

Follow conventional commits format:

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types**: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `chore`

**Examples**:
- `feat(crm): add customer contact management`
- `fix(users): resolve authentication token expiry`
- `docs(readme): update installation instructions`
- `test(crm): add tests for customer creation`
- `chore: update dependencies`

### Branch Naming

- Feature: `feature/short-description`
- Bug fix: `fix/short-description`
- Documentation: `docs/short-description`

### Testing Requirements

- All new features must include tests
- Maintain or improve code coverage
- Run tests before submitting PR: `make test`

### Documentation

- Update docstrings in Portuguese for domain logic
- Add comments for non-obvious code
- Update API documentation if endpoints change
- Update this README if adding new sections or commands

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

## Support

For issues and questions:
- Open an issue on GitHub
- Check existing documentation in the `docs/` directory
- Review the AGENTS.md file for development guidelines

## Authors

kerp development team
