#!/bin/bash

#Attention! - This will stop all running containers and delete them
echo -e "Stopp all running containers\n"
docker stop $(docker ps -aq)
echo -e "\nContainers stopped\n-----------\nStart deleting containers\n"
docker rm $(docker ps -aq)
echo -e "\nContainers deleted\n-----------\nStart deleting all cloud-inf images\n"
docker rmi cloud-inf_web cloud-inf_api cloud-inf_db
echo -e "\nImages deleted\n-----------\nStart deleting all cloud-inf networks\n"
docker network rm cloud-inf_intNetwork cloud-inf_dbNetwork
echo -e "\nNetworks deleted\n-----------"

echo -e "Building with docker-compose"
docker-compose up