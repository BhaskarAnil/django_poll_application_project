# Django Poll Application Project

This is a simple Django-based poll application. It allows users to view polls and vote on them, and provides an admin interface for managing polls and choices.

## Features

- Public site to view polls and vote
- Admin site to add, change, and delete polls
- User authentication for admin actions

## Project Structure

```text
poll_app_project/           # Main project folder (repo root)
├── poll_app/               # Django project folder (settings, wsgi, asgi, urls)
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── my_poll/                # Django app folder (polls app)
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   ├── static/
│   └── templates/
├── db.sqlite3              # SQLite database (ignored by git)
├── manage.py               # Django management script
├── requirements.txt        # Python dependencies
├── .gitignore              # Git ignore rules
└── ReadMe.md               # Project documentation (this file)
```

- **poll_app/**: The Django project folder containing global settings and configuration.
- **my_poll/**: The Django app folder containing the poll application logic, models, views, templates, and static files.
- **db.sqlite3**: The SQLite database file (not tracked by git).
- **requirements.txt**: List of required Python packages.

## Getting Started

### Clone the repository

```bash
git clone git@github.com:BhaskarAnil/django_poll_application_project.git
cd django_poll_application_project
```

### Set up a virtual environment (recommended)

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run migrations

```bash
python manage.py migrate
```

### Create a superuser (for admin access)

```bash
python manage.py createsuperuser
```

### Start the development server

```bash
python manage.py runserver
```

- Visit `http://127.0.0.1:8000/` to access the polls app.
- Visit `http://127.0.0.1:8000/admin/` to access the admin site.


