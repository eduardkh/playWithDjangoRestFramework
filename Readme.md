# Initial Steps

## Initiate git

`git init`

## Create a virtual environment and install django


```
pipenv install pep8 --dev
pipenv install autopep8 --dev
pipenv install django
pipenv install djangorestframework
pipenv shell
pip freeze > requirements.txt (optional)
```

## Install requirements (optional)

`pip install -r requirements.txt`

## Create Project
```
django-admin startproject api_example
cd api_example
```
## Check the server for the first time
```
manage.py migrate
manage.py runserver
```
## Create App
```
manage.py startapp languages
```
## Create super-user
```
manage.py createsuperuser
```