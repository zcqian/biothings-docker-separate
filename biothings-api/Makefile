BIOTHINGS_VERSION ?= 0.9.0

biothings : Dockerfile
	docker build \
		--build-arg BIOTHINGS_VERSION=${BIOTHINGS_VERSION} \
		-t biothings:${BIOTHINGS_VERSION} .
