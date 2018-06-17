LOCAL SETUP

https://docs.docker.com/install/linux/docker-ce/ubuntu/#docker-ee-customers

https://askubuntu.com/questions/1030179/package-docker-ce-has-no-installation-candidate-in-18-04

sudo su postgres

createuser -d -SRP catalog #digite a senha

createdb -O catalog catalog

docker run --env-file=docker.env --network=host -it marcelotokarnia/trackpedia:0.0.8 --prod

Deployed at https://206.189.199.113/