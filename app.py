from flask import Flask
from flask import json
import logging

app = Flask(__name__)


@app.route("/")
def hello():
    app.logger.info('Main request successfull')
    return "Hello World!"


@app.route("/status")
def status():
    app.logger.info('Status check successfull')
    response = app.response_class(
        response=json.dumps({"result": "OK - healthy"}),
        status=200,
        mimetype="application/json",
    )
    return response


@app.route("/metrics")
def metrics():
    app.logger.info('Metrics check successfull')
    response = app.response_class(
        response=json.dumps(
            {
                "status": "success",
                "code": 0,
                "data": {"UserCount": 140, "UserCountActive": 23},
            }
        ),
        status=200,
        mimetype="application/json",
    )
    return response


if __name__ == "__main__":
    logging.basicConfig(filename='app.log', level=logging.INFO)
    app.run(host="0.0.0.0")
