import datetime

from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def hello_world():
    now = datetime.datetime.now()
    return jsonify({
        "message": "Hello World!",
        "now": now
    })


if __name__ == '__main__':
    app.run()
