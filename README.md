# DRCSYSTEM
# create a virtual enviorment
conda create --name Mydjangoenv django
conda install django

#connected mysql with Django
# Install Library
pip install mysqlclient
# Create database in mysql
CREATE DATABASE mysqldrc;

# create a project
django-admin startproject myproject

# create a app
python manage.py startapp loginapp
# chnage the database code in Django settings.py file
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "mysqldrc", # add database name
        'USER': "root", # add root name
        'PASSWORD': "jigu2103", # addpassword
        'HOST': "127.0.0.1",
        'PORT': "3306",
    }
}

# do a migration 
python manage.py migrate

# check database
USE mysqldrc;
SHOW tables;

# settings.py
join the dir for templates
and add loginapp in app

# created a template folder inside loginapp folder
# Templates
this folder contains welcome.html,login and register.html

# urls.py
created url pattern for html files

# Models.py
register User model in model.py file

# apply migrations
check migration folder whether it is been updated or not

# views.py
created a views for login and register 

#backend.py
check if the data are matched with the database, do the authentication with User model

# settings.py
add backend file authentictaion to the setting file

# create a super user
python manage.py createsuperuser # to view django adminstartion

# Run the file
# python manage.py make migrations
# python manage.py migrate
# python manage.py runserver
