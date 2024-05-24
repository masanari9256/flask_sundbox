.PHONY: setup-dev setup-prd build-dev build-prd up-dev ps down python

# dev環境をビルドして立ち上げる
setup-dev:
	@make build-dev
	@make up-dev
	@make ps

# prd環境をビルドして立ち上げる
setup-prd:
	@make build-prd
	@make up-prd
	@make ps

# dev環境のビルド
build-dev:
	docker compose -f compose.yaml -f compose.dev.yaml build --no-cache

# prd環境のビルド
build-prd:
	docker compose -f compose.yaml -f compose.prd.yaml build --no-cache

# dev環境の立ち上げ
up-dev:
	docker compose -f compose.yaml -f compose.dev.yaml up -d

# prd環境の立ち上げ
up-prd:
	docker compose -f compose.yaml -f compose.prd.yaml up -d

# コンテナの状態を確認
ps:
	docker compose ps

# コンテナを停止する
down:
	docker compose down

# pythonが使用できるコンテナに入る
python:
	docker compose exec app bash
