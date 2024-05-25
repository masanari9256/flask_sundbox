import datetime
import os
import requests
import json
from flask import Flask, jsonify

app = Flask(__name__)
app.json.ensure_ascii = False


@app.get("/")
def hello_world():
    now = datetime.datetime.now()
    print("うんちうんち")

    return jsonify({
        "message": "Hello World!",
        "now": now,
        "env": os.getenv('FLASK_ENV'),
    })


@app.get("/post_data/<id>")
def api_test(id):
    url = "https://jsonplaceholder.typicode.com/posts/"

    headers = {
        "Content-type": "application/json; charset=UTF-8"
    }

    data = {
        "title": "foo",
        "body": "bar",
        "userId": id
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    # レスポンスデータを取得
    response_data = response.json()

    return jsonify(response_data)


if __name__ == '__main__':
    debug = os.getenv('FLASK_ENV') == 'development'
    app.run(debug=debug, host='0.0.0.0', port=5000)
    # app.run(debug=True, host='0.0.0.0', port=5001)
