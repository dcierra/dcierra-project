# To run locally:
## Create a Python virtual environment:
> python -m venv djangoenv
## Activate virtual environment:
> source djangoenv/bin/activate
## Clone repository:
> git clone https://github.com/dcierra/dcierra-project.git
## cd to directory:
> cd dcierra-project
## Install requirements:
> pip install -r requirements.txt
## Copy .env.example to .env:
> cp .env.example .env
## fill .env
## Create database
## Make migrations:
> python manage.py makemigrations
## Migrate:
> python manage.py migrate
## Create a superuser:
> python manage.py createsuperuser
## Run server:
> python manage.py runserver
