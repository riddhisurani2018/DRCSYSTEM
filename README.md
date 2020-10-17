# DRCSYSTEM
Step - 1
#create a virtual enviorment
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

# step- 2
# created a template folder inside loginapp folder
# Templates
this folder contains welcome.html,login and register.html

# urls.py
created url pattern for html files

# Models.py
register User model in model.py file

# views.py
created a views for login and register 

#backend.py
check if the data are matched with the database, do the authentication with User model

# create a super user
python manage.py createsuperuser # to view django adminstartion

# Run the file
python manage.py make migrations
python manage.py mograte
python manage.py runserver
