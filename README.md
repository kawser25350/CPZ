# CPZ (Community Posts Zone)

A modern Django publishing platform where users can write posts, organize them with categories, and manage their own content from a profile dashboard.

CPZ is designed for fast iteration in development and straightforward deployment in production.

## Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Screenshots](#screenshots)
- [Quick Start](#quick-start)
- [Configuration](#configuration)
- [Common Commands](#common-commands)
- [Routes](#routes)
- [Deployment](#deployment)
- [Troubleshooting](#troubleshooting)
- [Roadmap Ideas](#roadmap-ideas)
- [License](#license)

## Overview

CPZ provides:

- user authentication (register, login, logout)
- profile management
- password change flow
- post creation/edit/delete with ownership rules
- category-based filtering on the home feed

The UI is built with Django templates, Bootstrap 5, and crispy forms.

## Key Features

- Secure auth flows using Django auth
- Author-only post editing and deletion
- "My Posts" dashboard for each user
- Category tagging for posts (many-to-many)
- Search and category filtering from the home page
- Responsive template-based frontend

## Tech Stack

- Backend: Django 6.0.4
- Database:
  - SQLite by default (local/dev)
  - PostgreSQL-ready via `dj-database-url` and `psycopg`
- Frontend: Django Templates + Bootstrap 5
- Forms: `django-crispy-forms` + `crispy-bootstrap5`
- App server (prod): Gunicorn

## Project Structure

```text
CPZ/
  CPZ/                # Project settings, urls, wsgi/asgi
  author/             # Auth, profile, my-posts flows
  posts/              # Post CRUD logic
  category/           # Category model and related logic
  templates/          # Global templates
  static/             # Source static assets
  manage.py
  requirements.txt
```

## Screenshots

Place screenshots in `docs/screenshots/` with these exact names:

- `home-page.png`
- `profile-page.png`
- `add-post-page.png`

### Home Page

![Home Page](docs/screenshots/home-page.png)

### Profile Page

![Profile Page](docs/screenshots/profile-page.png)

### Add Post Page

![Add Post Page](docs/screenshots/add-post-page.png)

## Quick Start

### 1. Clone

```bash
git clone https://github.com/kawser25350/C-P-Z.git
cd C-P-Z
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
```

Activate it:

- Windows (PowerShell):

```powershell
.\.venv\Scripts\Activate.ps1
```

- Windows (cmd):

```bat
.venv\Scripts\activate.bat
```

- macOS/Linux:

```bash
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Migrations

```bash
python manage.py migrate
```

### 5. (Optional) Create Admin User

```bash
python manage.py createsuperuser
```

### 6. Start the App

```bash
python manage.py runserver
```

Open: http://127.0.0.1:8000/

## Configuration

The project reads configuration from environment variables.

| Variable | Required | Default | Purpose |
|---|---|---|---|
| `DJANGO_SECRET_KEY` | Production: Yes | Django dev key | Django secret key |
| `DJANGO_DEBUG` | No | `True` | Debug mode toggle |
| `DJANGO_ALLOWED_HOSTS` | Production: Yes | `*` | Comma-separated hosts |
| `DATABASE_URL` | No | SQLite file | Database connection string |

Example `.env` values for production:

```env
DJANGO_SECRET_KEY=replace-with-a-strong-secret
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=your-domain.com,www.your-domain.com
DATABASE_URL=postgresql://user:password@host:5432/dbname
```

## Common Commands

```bash
python manage.py runserver
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic --noinput
python manage.py check
```

## Routes

High-level route map:

- `/` home feed
- `/admin/` Django admin
- `/posts/` post create/edit/delete
- `/author/` auth, profile, password change, my posts
- `/category/` category routes

## Deployment

This project is provider-agnostic. The same production flow works across platforms.

### Production Checklist

1. Set production environment variables
2. Use PostgreSQL (recommended)
3. Run migrations
4. Collect static files
5. Start with Gunicorn

Build/start sequence:

```bash
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate
gunicorn CPZ.wsgi:application
```

### Railway

Use the same build/start commands as above.

Set service variables:

- `DJANGO_SECRET_KEY`
- `DJANGO_DEBUG=False`
- `DJANGO_ALLOWED_HOSTS=<your-railway-domain>`
- `DATABASE_URL=<railway-postgres-url>`

### VPS (Ubuntu + Nginx + Gunicorn)

Typical flow:

1. Clone project and create virtualenv
2. Install requirements
3. Configure env vars
4. Run `collectstatic` and `migrate`
5. Run Gunicorn via systemd
6. Reverse proxy through Nginx

## Troubleshooting

### Static assets not updating

- Hard refresh browser (`Ctrl+F5`)
- Re-run `collectstatic` in production
- Confirm the template points to the expected static file names

### `DisallowedHost` error

Set `DJANGO_ALLOWED_HOSTS` correctly (comma-separated).

### Database connection errors

Check `DATABASE_URL` format and verify PostgreSQL credentials/network access.

### Crispy form template errors

Ensure `django-crispy-forms` and `crispy-bootstrap5` are installed and present in `INSTALLED_APPS`.

## Roadmap Ideas

- Automated tests for auth and CRUD permissions
- Pagination on home feed
- Rich text editor for posts
- Post reactions and comments
- Role-based moderation features

## License

This project is licensed under the MIT License. If a `LICENSE` file is present in the repository, see it for full terms.
