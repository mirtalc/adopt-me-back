## Docker volume information

Volumes (also named volumes) are stored here:\
`/var/lib/docker/volumes/`

- docker volume ls
- docker volume rm my-volume

## Start only postgres docker

docker-compose -f docker-compose.db.yml up

## Start both postgres & django docker

docker-compose up

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

First time
