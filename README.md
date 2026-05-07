# C-P-Z

A Django-based content publishing project featuring user authentication, profile management, and CRUD workflows for posts. The UI is built with Django templates and styled using Bootstrap 5 via `dj[...]

## Features

- Authentication: register, login, logout
- User profile: update profile details
- Password management: change password while staying logged in
- Posts:
  - create posts (authenticated users)
  - edit/delete only your own posts
  - view "My Posts" dashboard
- Categories:
  - posts can be assigned to one or more categories
  - home page filtering by category (via query parameter)

## Tech Stack

- Backend: Django 6.0.4
- Database: SQLite (default)
- Frontend: Django Templates
- Forms/UI: `django-crispy-forms` + `crispy-bootstrap5`

## Project Structure

- `CPZ/` — Django project (settings, URLs, base views)
- `posts/` — post model + create/edit/delete views
- `author/` — authentication, profile, and user dashboard
- `category/` — category model (and future category views)
- `templates/` — HTML templates
- `static/` — local static assets (development)

## Requirements

- Python 3.10+ recommended
- pip / virtualenv

Dependencies are listed in `requirements.txt`.

## Setup (Local Development)

1. Clone the repository

   ```bash
   git clone https://github.com/kawser25350/C-P-Z.git
   cd C-P-Z
   ```

2. Create and activate a virtual environment

   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS/Linux
   source .venv/bin/activate
   ```

3. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations

   ```bash
   python manage.py migrate
   ```

5. Create an admin user (optional)

   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server

   ```bash
   python manage.py runserver
   ```

Open `http://127.0.0.1:8000/`.

## Usage

- Home (`/`) lists posts and supports filtering by category.
- Register/Login is available under the `/author/` routes.
- Add Post: `/posts/add/` (login required)
- My Posts: `/author/posts/` (login required)

## URL Routes (High Level)

- `/` — home
- `/admin/` — Django admin
- `/posts/` — post creation/edit/delete
- `/author/` — login, register, profile, password change, my posts
- `/category/` — reserved for category-related endpoints

## Notes

- This project uses SQLite by default (`db.sqlite3`). For production, configure a production-grade database and update `ALLOWED_HOSTS`, `DEBUG`, and `SECRET_KEY`.
- Static files are configured with `STATICFILES_DIRS` and `STATIC_ROOT` for `collectstatic`.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
