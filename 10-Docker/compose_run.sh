#!/bin/bash

#Attention! - This will stop all running containers and delete them
echo -e "Stopp all running containers\n"
docker stop $(docker ps -aq)
echo -e "\nContainers stopped\n-----------\nStart deleting containers\n"
docker rm $(docker ps -aq)
echo -e "\nContainers deleted\n-----------\nStart deleting all cloud-inf images\n"
docker rmi 10-docker_api 10-docker_web 10-docker_db
echo -e "\nImages deleted\n-----------"

echo -e "Building with docker-compose"
docker-compose up