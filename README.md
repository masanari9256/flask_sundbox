# Flaskのサンドボックス環境

## 環境構築

### dev環境

- flaskの開発サーバ + Nginxを使用
- 開発を進めるときは、以下のコマンドで環境を立ち上げる
  ```
  make setup-dev
  ``` 
- コンテナが動いていることを確認し、以下のアドレスにアクセス  
  http://127.0.0.1:80

- 開発を終了する場合は、以下のコマンドで環境を停止できる
  ```
  make down
  ``` 
- その他、使用しそうなdockerコマンドは[Makefile](Makefile)を見る

### prd環境

- flaskの開発サーバ + uWSGI + Nginxを使用
- 開発を進めるときは、以下のコマンドで環境を立ち上げる
  ```
  make setup-prd
  ``` 
- コンテナが動いていることを確認し、以下のアドレスにアクセス  
  http://127.0.0.1:80
- 開発を終了する場合は、以下のコマンドで環境を停止できる
  ```
  make down
  ```
- その他、使用しそうなdockerコマンドは[Makefile](Makefile)を見る

# 参考サイトなど

- https://qiita.com/yoshi-kin/items/c5a2a4ddb45adfd00fce
