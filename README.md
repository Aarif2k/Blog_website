# Blog_website

Overview
Blog Website is a modern web application built with Django, designed for creating, managing, and displaying blog posts. It provides an intuitive platform for authors to write and publish articles, and for readers to browse, search, and interact with content.

Features
User Authentication: Users can sign up, log in, and manage their profiles.
Blog Management: Authors can create, edit, and delete blog posts.
Post Categories and Tags: Organize posts with categories and tags for easy navigation.
Search Functionality: Search for posts by title, content, or tags.
Responsive Design: Optimized for both desktop and mobile devices.
Admin Panel: Manage posts, categories, and user accounts through the Django admin interface.

Technologies Used
Backend:
Django: Web framework for building the application.
MySQL: Database for storing blog data.
Frontend:
HTML, CSS, JavaScript: Core technologies for the user interface.
Bootstrap/Django Crispy Forms: For styling and form rendering (optional, based on your choice).

Installation
Prerequisites
asgiref==3.8.1
Django==5.0.7
django-pagination==1.0.7
Faker==26.0.0
mysqlclient==2.2.4
python-dateutil==2.9.0.post0
six==1.16.0
sqlparse==0.5.0
tzdata==2024.1
whitenoise==6.7.0
Virtual Environment (recommended)
Setup Instructions
Clone the Repository:

git clone https://github.com/Aarif2k/blog_website.git
cd blog_website
Create and Activate a Virtual Environment:

python -m venv venv
venv\Scripts\activate
Install Dependencies:

pip install -r requirements.txt

Configure Database:

Update the DATABASES setting in settings.py with your MySQL credentials.
Apply migrations:
python manage.py migrate

Create a Superuser:
python manage.py createsuperuser

Run the Development Server:
python manage.py runserver

Access the Website:
Open your web browser and go to http://127.0.0.1:8000/ to view the website.

Usage
Admin Panel
Access the admin panel at http://127.0.0.1:8000/admin/ using the superuser credentials you created. Here, you can manage blog posts, categories, tags, and user accounts.

User Interface
Read Blog Posts: Browse and read blog posts.
Write Posts: Authors can create and manage their posts from the admin panel or a dedicated author interface.
