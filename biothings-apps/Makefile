APP_GIT_TAG ?= master

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
