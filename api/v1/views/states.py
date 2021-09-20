#!/usr/bin/python3
""" objects """
from flask import Flask, Blueprint, jsonify, request, abort, make_response
from api.v1.views import app_views
from models import storage
from models.state import State


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def retrieve():
    """ Retrieves the list of all State objects """
    states = []
    for x in storage.all('State').values():
        states.append(x.to_dict())
    return jsonify(states)


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def retrive_id(state_id=None):
    """ Retrieves a State object
    If the state_id is not linked to any State object,raise a 404 error """
    single_states = storage.get(State, state_id)
    if single_states is None:
        abort(404)
    return jsonify(single_states.to_dict())


@app_views.route('/states/<state_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete(state_id):
    """ Deletes a state
    If the state_id is not linked to any State object, raise a 404 error
    Returns an empty dictionary with the status code 200 """
    try:
        states = storage.get(State, state_id)
        storage.delete(states)
        states.save()
        return jsonify({}), 200
    except Exception:
        abort(404)


@app_views.route('/states/', methods=['POST'], strict_slashes=False)
def post():
    """Creates a state"""
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    if "name" not in request.get_json():
        return make_response(jsonify({'error': 'Missing name'}), 400)


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def put_state(state_id):
    """Updates a state"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    if not request.json:
        return jsonify({"error": "Not a JSON"}), 400
    for key, value in request.get_json().items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(state, key, value)
    state.save()
    return jsonify(state.to_dict()), 200
