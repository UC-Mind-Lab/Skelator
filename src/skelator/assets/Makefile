TAG=IMAGE_NAME

all: docker

docker:
	docker build -t $(TAG) docker

repair.log: docker
	darjeeling repair repair.yml --continue --verbose | tee $@

coverage.json: docker
	darjeeling coverage coverage.yml --format json | tee $@

negations.json: docker
	darjeeling negations coverage.yml --format json --linkage LINKAGE | tee $@ 

attach: docker
	docker run -it $(TAG) /bin/bash

clean:
	docker image rm -f $(TAG)


.PHONY: clean coverage docker repair
