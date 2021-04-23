#
# common
# NOTE: not to be use independtly
#

HIDE ?= @
SHELL := /bin/bash
REGISTRY ?= registry.gitlab.com/spartanio # TODO
BRANCH_NAME ?= master #$(shell git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/\1/')

push:
	$(HIDE)docker tag $(DOCKER_IMAGE) $(REGISTRY):${BRANCH_NAME}
	$(HIDE)docker push $(REGISTRY):${BRANCH_NAME}
	$(HIDE)docker rmi $(REGISTRY):${BRANCH_NAME}
	-$(HIDE)docker rmi $(DOCKER_IMAGE)

pull:
	$(HIDE)docker pull $(REGISTRY):$(BRANCH_NAME)
	$(HIDE)docker tag  $(REGISTRY):$(BRANCH_NAME) $(DOCKER_IMAGE)

login:
	$(HIDE)docker login --username $(CI_REGISTRY_USER) --password $(CI_REGISTRY_PASSWORD) $(REGISTRY)

restart:
	$(HIDE)docker restart $(DOCKER_CONTAINER)

stop:
	$(HIDE)$(MAKE) stop.$(DOCKER_CONTAINER)

stop.%:
	$(HIDE)docker rm -f $*

enter.%:
	$(HIDE)docker exec -it $* sh -c 'test -e /bin/bash && /bin/bash || sh'

enter:
	$(HIDE)$(MAKE) enter.$(DOCKER_CONTAINER)

clean-all:
	-$(HIDE)docker ps -aq | xargs docker stop
	-$(HIDE)docker ps -aq | xargs docker rm
	-$(HIDE)docker images -q| xargs docker rmi

clean-containers:
	-$(HIDE)docker ps -aq | xargs docker stop
	-$(HIDE)docker ps -aq | xargs docker rm

clean:
	-$(HIDE)docker rmi $(docker images |grep --color=always none|xargs -n1|grep -A1 none|grep -Ev 'none|--')

ctop:
	$(HIDE)docker run --rm -ti --name=ctop -v /var/run/docker.sock:/var/run/docker.sock quay.io/vektorlab/ctop:latest
