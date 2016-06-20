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


brew install mysql

pip install MySQL-python




### Update DB settings in project/config.py

1. `SECRET_KEY`
1. `SQLALCHEMY_DATABASE_URI`



### Run

```sh
$ python manage.py runserver
```




