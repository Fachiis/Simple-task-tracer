****Simple Task Tracker****
-
>A simple task tracker that allows users to create tasks and associate them with it with a team. The team leader of the team will assign the team members to the tasks.The team members will update the status of the task.

## Features

- Django 4.0, Python 3.9, Djangorestframework 3.13, Djangorestauth 0.9, Celery 5.2, RabbitMQ
- Install via [Pipenv](https://pypi.org/project/pip/)
- User login and logout
- Admin interface

The code style used for the project is PEP 8 -- Style Guide for Python Code and black: For Style Guide
Enforcement.

---
## Table of Contents
* **[Installation](#installation)**
  * [Pipenv](#pip)
* [Setup](#setup)

---
## Installation
The application can be installed via Pipenv. To start,
clone the repo to your local computer and change into the proper directory.

```
$ git clone https://github.com/Fachiis/Simple-task-tracer.git
$ cd Simple-task-tracer
```
```
$ pipenv install
$ pipenv shell
(Simple_task_tracker) $ python manage.py migrate
(Simple_task_tracker) $ python manage.py createsuperuser
(Simple_task_tracker) $ python manage.py runserver

# Load the site at http://127.0.0.1:8000/api/v1/
```

Open another terminal and run the following commands to start the celery server. Make sure message broker (either RabbitMQ or Redis) is running.

```
(Simple_task_tracker) $ celery -A simple_task_tracker worker -l info
```
## Setup

```
# Run Migrations
(Simple_task_tracker) $ python manage.py migrate

# Create a Superuser
(Simple_task_tracker) $ python manage.py createsuperuser

# Start Django Server:
(Simple_task_tracker) $ python manage.py runserver

Confirm the RabbitMQ or Redis server is running.

# Start Celery Server:
(Simple_task_tracker) $ celery -A simple_task_tracker worker -l info

Confirm everything is running and working.
# Load the site at http://127.0.0.1:8000/api/v1/
```
Enjoy the Simple_task_tracker!