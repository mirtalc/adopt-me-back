## Environmental variables information

Django gets environmental variables differently depending on if you're running the server directly or through the container.

- a) Directly: it gets the values from the _.env_ file (untracked by git)
- b) Dockerized: it gets the values from the _environment_ section of the docker-compose file (which, in turn, are either staticly setted or take them from the _.env_ file).

This is important because, for example, HOST variable is different in these two situations).

## Docker volume information

Volumes (also named volumes) are stored here:\
`/var/lib/docker/volumes/`

- docker volume ls
- docker volume rm my-volume

## Start only postgres docker

docker-compose -f docker-compose.db.yml up

Then, if you want to run docker, be sure to be in a virtual environment (`pipenv shell`) and then run the Django web server:

`python manage.py runserver`

(If you have new dependencies, remember to install them with `pipenv install` before running the server).

- Django settings > 'DATABASE > 'HOST': should be 'localhost'. If value is 'db', you get this error: `django.db.utils.OperationalError: could not translate host name "db" to address: Temporary failure in name resolution`

- Django commands execution: Directly from your virtual environment.

## Start both postgres & django docker

docker-compose up

- Django settings > 'DATABASE > 'HOST': should be 'db' (i.e., the name of the dockerized service). That's why it's setted directly on the docker-compose file.

## Remove postgres data from volume

docker-compose -f docker-compose.db.yml down -v

# Docker + Postgres configuration

1. Create a file _docker-compose.yml_ with this content:
   //TODO

2. Create a file _Dockerfile_ with this content:
   //TODO

3. Create a file _requirements.txt_ with this content:
   //TODO

[Optional] If we want to only dockerize the database:

4. Create a file _docker-compose.db.yml_ with this content:

---
