all: docker_status docker_build
docker_status:
	@docker ps 
docker_build:
	@docker build -t test:v1 . 
