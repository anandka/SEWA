# SEWA application

[![Build Status](https://travis-ci.org/mjhea0/flask-basic-registration.svg?branch=master)](https://travis-ci.org/mjhea0/flask-basic-registration)

Starter app for managing users - login/logout and registration.

## QuickStart

### Set Environment Variables

```sh
$ export APP_SETTINGS="project.config.DevelopmentConfig"
```

or

```sh
$ export APP_SETTINGS="project.config.ProductionConfig"
```

### Download Required modules
Go to the root folder of application
install pip by command -  sudo apt-get install python-pip
execute  - pip install -r requirements.txt



### Update Settings in Production

1. `SECRET_KEY`
1. `SQLALCHEMY_DATABASE_URI`

### Create DB

```sh
$ python manage.py create_db
$ python manage.py db init
$ python manage.py db migrate
$ python manage.py create_admin
```

### Run

```sh
$ python manage.py runserver
```

