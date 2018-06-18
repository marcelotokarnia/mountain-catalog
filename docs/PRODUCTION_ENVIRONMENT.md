# TREKKPEDI

## Production Environment

In the future we aim to do it with Ansible

https://docs.docker.com/install/linux/docker-ce/ubuntu/#docker-ee-customers

https://askubuntu.com/questions/1030179/package-docker-ce-has-no-installation-candidate-in-18-04

[Set your database](./LOCAL_SETUP_EXPLAINED.md)

docker run --env-file=docker.env --network=host -it marcelotokarnia/trackpedia:$TAG$ --prod