# DRCSYSTEM
Step - 1
#connected mysql with Django
# Install Library
pip install mysqlclient
# Create database in mysql
CREATE DATABASE mysqldrc;
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
