APP_GIT_TAG ?= master
BIOTHINGS_VERSION ?= 0.9.1

biothings-hub:
	docker build \
		--build-arg API_NAME=biothings-hub \
		--build-arg APP_GIT="https://github.com/zcqian/biothings-standalone-hub.git" \
		--build-arg APP_TAG=${APP_GIT_TAG} \
		-t vanilla-hub:${APP_GIT_TAG} .

mygeneset-hub: Dockerfile
	docker build \
		--build-arg BIOTHINGS_VERSION=${BIOTHINGS_VERSION} \
		--build-arg API_NAME=mygeneset.info \
		--build-arg APP_GIT="https://github.com/biothings/mygeneset.info" \
		--build-arg APP_TAG=${APP_GIT_TAG} \
		-t $@:${APP_GIT_TAG} .

biothings-mygene:
	docker build \
		--build-arg API_NAME=mygene.info \
		--build-arg APP_GIT="https://github.com/biothings/mygene.info.git" \
		--build-arg APP_TAG=${APP_GIT_TAG} \
		-t mygene-hub:${APP_GIT_TAG} .

biothings-mychem:
	docker build \
		--build-arg API_NAME=mychem.info \
		--build-arg APP_GIT="https://github.com/biothings/mychem.info.git" \
		--build-arg APP_TAG=${APP_GIT_TAG} \
		-t mychem-hub:${APP_GIT_TAG} .

biothings-myvariant:
	docker build \
		--build-arg API_NAME=myvariant.info \
		--build-arg APP_GIT="https://github.com/biothings/myvariant.info.git" \
		--build-arg APP_TAG=${APP_GIT_TAG} \
		-t myvariant-hub:${APP_GIT_TAG} .


outbreak:
	docker build \
		--build-arg API_NAME=mydisease.info \
		--build-arg BIOTHINGS_VERSION=${BIOTHINGS_VERSION} \
		--build-arg APP_GIT="https://github.com/biothings/mydisease.info.git" \
		--build-arg APP_TAG=${APP_GIT_TAG} \
		-t myvariant-hub:${APP_GIT_TAG} .
