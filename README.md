<div align="center">

# Django Blog

**A full-featured blog platform built with Django 6 and Bootstrap 5**

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-6-092E20?style=flat-square&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5-7952B3?style=flat-square&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)

[Features](#features) · [Tech Stack](#tech-stack) · [Getting Started](#getting-started) · [Usage](#usage) · [Contributing](#contributing)

</div>

---

## Overview

Django Blog is an open-source blogging application with a public-facing frontend for readers and a protected dashboard for administrators. It supports post management, category browsing, full-text search, user authentication, and media uploads — ready to run locally or deploy to production.

---

## Screenshots

| Login | Home Page |
|---|---|
| ![Login](https://github.com/user-attachments/assets/c323b864-c85b-4eb6-a218-0e72be4b62a9) | ![Home](https://github.com/user-attachments/assets/21b95113-ce9b-48db-bdd7-1a3a8ecf8f90) |

| Admin Dashboard | Blog Detail |
|---|---|
| ![Dashboard](https://github.com/user-attachments/assets/605ca177-e790-4094-b5bb-61db26e7bad7) | ![Detail](https://github.com/user-attachments/assets/781674cc-af25-4005-a1e1-c846f8ae04d9) |

---

## Features

**Public Frontend**
- Home page with featured and latest blog posts
- Blog detail page with full content and comments section
- Browse posts by category
- Full-text search across post titles, descriptions, and body
- User registration and login/logout

**Admin Dashboard**
- Overview stats (total posts and categories)
- Full CRUD for blog posts — with featured image upload, status toggle, and featured flag
- Full CRUD for categories
- User management (add, edit, delete users)
- Login-protected routes

**Other**
- About section and social links managed from the database
- Auto-generated slugs for blog post URLs
- Draft / Published status for posts
- Featured post flag to highlight posts on the home page
- Media file uploads with date-based directory organization
- Custom 404 error page

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python 3, Django 6 |
| Frontend | Bootstrap 5, custom CSS |
| Forms | django-crispy-forms + crispy-bootstrap5 |
| Database | SQLite (default) |
| Storage | Local media & static file serving |

---

## Getting Started

### Prerequisites

- Python 3.9+
- pip

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/shadows12-star/Django-Blog.git
cd Django-Blog/blog_main
```

**2. Create and activate a virtual environment**

```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
```

**3. Install dependencies**

```bash
pip install django pillow crispy-bootstrap5 django-crispy-forms
```

**4. Apply migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

**5. Create a superuser**

```bash
python manage.py createsuperuser
```

**6. Run the development server**

```bash
python manage.py runserver
```

Open [http://127.0.0.1:8000/home/](http://127.0.0.1:8000/home/) in your browser.

---

## Usage

| URL | Description |
|---|---|
| `/home/` | Blog home page |
| `/details/<slug>/` | Individual blog post |
| `/categories/<id>/` | Posts by category |
| `/search/?keyword=...` | Search posts |
| `/register/` | Create a new account |
| `/login/` | Log in |
| `/logout/` | Log out |
| `/dashboard/` | Admin dashboard (login required) |
| `/admin/` | Django built-in admin panel |

---

## Project Structure

```
Django-Blog/
└── blog_main/
    ├── blog_app/        # Public-facing blog — views, models, forms, URLs
    ├── dashboard/       # Admin dashboard — CRUD for posts, categories, users
    ├── blog_main/       # Project settings and root URL config
    ├── templates/       # HTML templates
    ├── static/          # CSS and static images
    ├── media/           # User-uploaded images (created at runtime)
    └── manage.py
```

---

## Configuration

> Before deploying to production, review the following settings in `blog_main/settings.py`.

| Setting | Notes |
|---|---|
| `SECRET_KEY` | Replace the default value with a strong, random key |
| `DEBUG` | Set to `False` in production |
| `ALLOWED_HOSTS` | Add your domain(s) for production deployments |
| Media files | Uploaded images are saved to `media/uploads/YYYY/MM/DD/` — ensure the directory is writable |
| Static files | Run `python manage.py collectstatic` before deploying |

---

## Contributing

Contributions are welcome! To get started:

1. Fork the repository
2. Create a feature branch — `git checkout -b feature/your-feature`
3. Commit your changes — `git commit -m 'Add your feature'`
4. Push to the branch — `git push origin feature/your-feature`
5. Open a Pull Request

Please open an issue first for major changes so we can discuss the approach.

---

<div align="center">

Made with ❤️ using Django · [View on GitHub](https://github.com/shadows12-star/Django-Blog)

</div>
