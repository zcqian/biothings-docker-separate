# Docker Images for BioThings
This repository contains Dockerfiles necessary to produce Docker images for BioThings.

## Using the SDK
To get started using the SDK, you need to have Docker and Docker Compose set up. Then, go to the `biothings-sdk-compose` directory and run `docker-compose up` launch the SDK.

You can access the BioThings Web App at http://<LOCALHOST_OR_IP_OF_DOCKER_HOST>:8080 . The BioThings Hub will be listening on port 7080 for HTTP and WebSocket requests, and on port 7022 for SSH connections. Persistent data will be located in the `biothings` directory in the persistent data volume.

In the persistent data volume, there will be the SSH host keys for BioThings Hub. Also, there will be logs and other useful information. To develop data plugins, place them into the `biothigns/biothings-standalone-hub/plugins` directory.

The docker compose file will run multiple containers, containing MongoDB listening on port 27017, ElasticSearch on port 9200, BioThings Web App on port 8080, and BioThings Hub on ports 7080 and 7022. An optional instance of Cerebro will be listenting on port 9000 for inspecting the ElasticSearch Data.

## Base Image

The base BioThings image contains only the biothings.api package and other necessary Python packages.
It is intended for building new APIs from scratch using the biothings.api.

## Individual API/Hubs