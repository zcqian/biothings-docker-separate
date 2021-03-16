BIOTHINGS_VERSION ?= 0.9.1

.PHONY: biothings
biothings : Dockerfile
	docker build \
		--build-arg BIOTHINGS_VERSION=${BIOTHINGS_VERSION} \
		-t biothings:${BIOTHINGS_VERSION} .

biothings-extradeveltools: biothings Dockerfile.extratools
	docker build \
		--build-arg BIOTHINGS_VERSION=${BIOTHINGS_VERSION} \
		-t biothings-extradeveltools:${BIOTHINGS_VERSION} .
