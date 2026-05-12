Django Blog
A full-featured blog web application built with Django and Bootstrap 5. It includes a public-facing blog frontend and a protected admin dashboard for managing posts, categories, and users.
________________________________________
Features
Public Frontend
•	Home page with featured and latest blog posts
•	Blog detail page with full content and comments section
•	Browse posts by category
•	Full-text search across post titles, descriptions, and body
•	User registration and login/logout
Admin Dashboard
•	Overview stats (total posts and categories)
•	Full CRUD for blog posts (with featured image upload, status toggle, featured flag)
•	Full CRUD for categories
•	User management (add, edit, delete users)
•	Login-protected routes — dashboard requires authentication
Other
•	About section and social links managed from the database
•	Auto-generated slugs for blog post URLs
•	Draft / Published status for posts
•	Featured post flag to highlight posts on the home page
•	Media file uploads with date-based directory organization
•	Custom 404 error page
________________________________________
Tech Stack
Layer	Technology
Backend	Python 3, Django 6
Frontend	Bootstrap 5, custom CSS
Forms	django-crispy-forms + crispy-bootstrap5
Database	SQLite (default)
Storage	Local media & static file serving
________________________________________
Project Structure
Django-Blog/
└── blog_main/
    ├── blog_app/           # Public-facing blog app (views, models, forms, URLs)
    ├── dashboard/          # Admin dashboard app (CRUD for posts, categories, users)
    ├── blog_main/          # Project settings and root URL config
    ├── templates/          # HTML templates (base, home, login, dashboard, etc.)
    ├── static/             # CSS and static images
    ├── media/              # User-uploaded images (created at runtime)
    └── manage.py
________________________________________
Getting Started
Prerequisites
•	Python 3.9+
•	pip
Installation
1.	Clone the repository
2.	git clone https://github.com/shadows12-star/Django-Blog.git
3.	cd Django-Blog/blog_main
4.	Create and activate a virtual environment
5.	python -m venv venv
6.	source venv/bin/activate      # On Windows: venv\Scripts\activate
7.	Install dependencies
8.	pip install django pillow crispy-bootstrap5 django-crispy-forms jupyterlab-server
9.	Apply migrations
10.	python manage.py makemigrations
11.	python manage.py migrate
12.	Create a superuser (for the Django admin panel and dashboard)
13.	python manage.py createsuperuser
14.	Run the development server
15.	python manage.py runserver
16.	Open your browser and go to http://127.0.0.1:8000/home/
________________________________________
Usage
URL	Description
/home/	Blog home page
/details/<slug>/	Individual blog post
/categories/<id>/	Posts by category
/search/?keyword=...	Search posts
/register/	Create a new account
/login/	Log in
/logout/	Log out
/dashboard/	Admin dashboard (login required)
/admin/	Django built-in admin panel
________________________________________
Configuration Notes
•	Media files: uploaded images are saved to media/uploads/YYYY/MM/DD/. Make sure the media/ directory is writable.
•	Static files: run python manage.py collectstatic before deploying to production.
•	Secret key: replace the default SECRET_KEY in blog_main/settings.py before going to production.
•	Debug mode: set DEBUG = False and configure ALLOWED_HOSTS for production deployments.
________________________________________
Screenshots
Login:
 
<img width="975" height="500" alt="image" src="https://github.com/user-attachments/assets/c323b864-c85b-4eb6-a218-0e72be4b62a9" />


Home page:
<img width="975" height="632" alt="image" src="https://github.com/user-attachments/assets/21b95113-ce9b-48db-bdd7-1a3a8ecf8f90" />



 


Admin Dashboard:
<img width="975" height="655" alt="image" src="https://github.com/user-attachments/assets/605ca177-e790-4094-b5bb-61db26e7bad7" />

 














Blog_Detail:
<img width="975" height="796" alt="image" src="https://github.com/user-attachments/assets/781674cc-af25-4005-a1e1-c846f8ae04d9" />

 
________________________________________
Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.
1.	Fork the repo
2.	Create a feature branch (git checkout -b feature/your-feature)
3.	Commit your changes (git commit -m 'Add your feature')
4.	Push to the branch (git push origin feature/your-feature)
5.	Open a Pull Request
________________________________________

