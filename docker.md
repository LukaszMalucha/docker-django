### Docker

##### purge docker
docker system prune
___
##### all containers + history
docker ps --all
___
##### -a - print output
docker start -a hello-world
___
##### get logs output without restart
docker logs 123asdi123zxc
___
##### start container again
docker start -a 234sdz23waz
___
##### stop container
docker stop 123jlksdf213
docker kill 123jlksdf213
___
##### multi-command redis (-it)
docker run redis
docker exec -it 014284359sdaf redis-cli
___
##### open shell in container (sh)
docker exec -it 21349876zdf sh
CTRL-D
___
##### Docker IP
docker-machine ip
___
### DOCKER IMAGE
___
##### Build Image
docker build .
___
##### Run Container out of an image
docker run 13qdsdzf123
___
##### Tag Image
docker build -t johndoe/mytag:latest 
___
##### Run Container with port mapping
docker -p 8080:8080 run 13qdsdzf123
___
##### Run Dockerfile.dev
docker build -f Dockerfile.dev .
___
##### Docker volumes (WIN)
docker run -p 8080:8080 -v /app/node_modules -v $(pwd):/app -e CHOKIDAR_USEPOLLING=true 250132c330be
___
##### Attach to container
docker attach 123421xzxc
___



### DOCKER COMPOSE
___
##### Launch containers with docker-compose
docker-compose up -d
___
##### Stop containers with docker-compose
docker-compose down
___
##### Container status
docker-compose ps
___








