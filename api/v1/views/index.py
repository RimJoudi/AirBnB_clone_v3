#!/usr/bin/python3
""" Module Flask """
from flask import Flask, Blueprint, jsonify, request
from api.v1.views import app_views
from models import storage


@app_views.route('/status', methods=['GET'])
def status():
    if request.method == 'GET':
        return jsonify({"status": "OK"})


@app_views.route('/stats')
def count():
    """
        retrieves the number of each objects by type
    """

    dict = {}
    dictionary = {
        "Amenity": "amenities",
        "Place": "places",
        "State": "states",
        "City": "cities",
        "Review": "reviews",
        "User": "users"
    }

    for item in dictionary:
        count = storage.count(item)
        dict[dictionary.get(item)] = count
    return jsonify(dictionary)
