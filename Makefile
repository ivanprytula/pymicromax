# By declaring a target as .PHONY, you ensure that Make will run the associated commands every time you invoke that target,
# regardless of whether a file with the same name exists. This prevents any potential confusion if a file named <some_name>
# were to be created in the future.

.PHONY: help

help:  ## Show this help (color=yes)
	@grep --extended-regexp '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'





add-dev-gateway:  ## e.g., make add-dev-gateway dep=mypy
	uv --directory microservices/gateway add --dev $(dep)
