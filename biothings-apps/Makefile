APP_GIT_TAG ?= master
FRAMEWORK_GIT_TAG ?= master

biothings-hub:
	docker build \
		--build-arg API_NAME=biothings-hub \
		--build-arg APP_GIT="https://github.com/zcqian/biothings-standalone-hub.git" \
		--build-arg APP_TAG=${APP_GIT_TAG} \
		-t vanilla-hub:${APP_GIT_TAG} .

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

biothings-mydisease:
	docker build \
		--build-arg API_NAME=mydisease.info \
		--build-arg APP_GIT="https://github.com/biothings/mydisease.info.git" \
		--build-arg APP_TAG=${APP_GIT_TAG} \
		-t mydisease-hub:${APP_GIT_TAG} .

biothings-mygeneset:
	docker build \
		--build-arg API_NAME=mygeneset.info \
		--build-arg APP_GIT="https://github.com/biothings/mygeneset.info.git" \
		--build-arg APP_TAG=${APP_GIT_TAG} \
		-t mygeneset-hub:${APP_GIT_TAG} .

.PHONY: purge all
purge:
	docker rmi \
		vanilla-hub:${APP_GIT_TAG} \
		mygene-hub:${APP_GIT_TAG} \
		mychem-hub:${APP_GIT_TAG} \
		myvariant-hub:${APP_GIT_TAG} \
		mydisease-hub:${APP_GIT_TAG} \
		mygeneset-hub:${APP_GIT_TAG} \
all: biothings-standalone-hub biothings-mygene biothings-mychem