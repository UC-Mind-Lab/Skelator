TAG=IMAGE_NAME

all: docker

docker:
	docker build -t $(TAG) docker

repair: docker
	darjeeling repair repair.yml

coverage: docker
	darjeeling coverage coverage.yml

attach: docker
	docker run -it $(TAG) /bin/bash

clean:
	docker image rm -f $(TAG)


.PHONY: clean coverage docker repair
