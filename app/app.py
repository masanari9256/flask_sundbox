import datetime
import os
from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def hello_world():
    now = datetime.datetime.now()
    return jsonify({
        "message": "Hello World!",
        "now": now,
        "env": os.getenv('FLASK_ENV'),
    })


if __name__ == '__main__':
    debug = os.getenv('FLASK_ENV') == 'development'
    app.run(debug=debug, host='0.0.0.0', port=5000)
    # app.run()
