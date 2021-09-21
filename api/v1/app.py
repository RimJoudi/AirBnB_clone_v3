#!/usr/bin/python3
"""
runs a Flask web application
"""
from flask import Flask, jsonify, Response
from api.v1.views import app_views
from models import storage
from flask_cors import CORS
import os

app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={'/*': {'origins': '0.0.0.0'}})


@app.teardown_appcontext
def appcontext():
    return storage.close()


@app.errorhandler(404)
def pageNotFound():
    '''
        returns a JSON-formatted 404 status code response.
    '''
    return jsonify({"error": "Not found"}), 404


if __name__ == '__main__':
    app.run(host=os.getenv('HBNB_API_HOST', '0.0.0.0'),
            port=os.getenv('HBNB_API_PORT', 5000), threaded=True)
