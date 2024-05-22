.PHONY: setup-dev setup-prd build-dev build-prd up-dev ps down python

setup-dev:
	@make build-dev
	@make up-dev
	@make ps

setup-prd:
	@make build-prd
	@make up-prd
	@make ps

build-dev:
	docker compose -f compose.yaml -f compose.dev.yaml build --no-cache

build-prd:
	docker compose -f compose.yaml -f compose.prd.yaml build --no-cache

up-dev:
	docker compose -f compose.yaml -f compose.dev.yaml up -d

up-prd:
	docker compose -f compose.yaml -f compose.prd.yaml up -d

ps:
	docker compose ps

down:
	docker compose down

python:
	docker compose exec app bash
