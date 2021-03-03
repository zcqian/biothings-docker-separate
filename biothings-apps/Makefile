APP_GIT_TAG ?= master
FRAMEWORK_GIT_TAG ?= master

biothings-hub:
	docker build \
		--build-arg BIOTHINGS_TAG=${FRAMEWORK_GIT_TAG} \
		--build-arg API_NAME=biothings-hub \
		--build-arg APP_GIT="https://github.com/zcqian/biothings-standalone-hub.git" \
		--build-arg APP_TAG=${APP_GIT_TAG} \
		-t biothings-standalone-hub:${APP_GIT_TAG} .

biothings-mygene:
	docker build \
		--build-arg BIOTHINGS_TAG=${FRAMEWORK_GIT_TAG} \
		--build-arg API_NAME=mygene.info \
		--build-arg APP_GIT="https://github.com/biothings/mygene.info.git" \
		--build-arg APP_TAG=${APP_GIT_TAG} \
		-t biothings-mygene:${APP_GIT_TAG} .

biothings-mychem:
	docker build \
		--build-arg BIOTHINGS_TAG=${FRAMEWORK_GIT_TAG} \
		--build-arg API_NAME=mychem.info \
		--build-arg APP_GIT="https://github.com/biothings/mychem.info.git" \
		--build-arg APP_TAG=${APP_GIT_TAG} \
		-t biothings-mychem:${APP_GIT_TAG} .

biothings-myvariant:
	docker build \
		--build-arg BIOTHINGS_TAG=${FRAMEWORK_GIT_TAG} \
		--build-arg API_NAME=myvariant.info \
		--build-arg APP_GIT="https://github.com/biothings/myvariant.info.git" \
		--build-arg APP_TAG=${APP_GIT_TAG} \
		-t biothings-myvariant:${APP_GIT_TAG} .

biothings-mydisease:
	docker build \
		--build-arg BIOTHINGS_TAG=${FRAMEWORK_GIT_TAG} \
		--build-arg API_NAME=mydisease.info \
		--build-arg APP_GIT="https://github.com/biothings/mydisease.info.git" \
		--build-arg APP_TAG=${APP_GIT_TAG} \
		-t biothings-mydisease:${APP_GIT_TAG} .

biothings-mygeneset:
	docker build \
		--build-arg BIOTHINGS_TAG=${FRAMEWORK_GIT_TAG} \
		--build-arg API_NAME=mygeneset.info \
		--build-arg APP_GIT="https://github.com/biothings/mygeneset.info.git" \
		--build-arg APP_TAG=${APP_GIT_TAG} \
		-t biothings-mygeneset:${APP_GIT_TAG} .

.PHONY: purge all
purge:
	docker rmi \
		biothings-standalone-hub:${APP_GIT_TAG} \
		biothings-mygene:${APP_GIT_TAG} \
		biothings-mychem:${APP_GIT_TAG} \
		biothings-myvariant:${APP_GIT_TAG} \
		biothings-mydisease:${APP_GIT_TAG} \
		biothings-mygeneset:${APP_GIT_TAG} \
all: biothings-standalone-hub biothings-mygene biothings-mychem