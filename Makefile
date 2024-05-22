.PHONY: setup build up ps down python

setup:
	@make build
	@make up
	@make ps

build:
	docker compose -f compose.yaml build --no-cache

up:
	docker compose up -d

ps:
	docker compose ps

down:
	docker compose down

python:
	docker compose exec app bash
