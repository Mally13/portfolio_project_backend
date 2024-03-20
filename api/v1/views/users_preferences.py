#!/usr/bin/python3
""" objects that handle all default RestFul API actions for User - Preference """
from models.user import User
from models.preference import Preference
from models import storage
from api.v1.views import app_views
from os import environ
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('users/<user_id>/preferences', methods=['GET'],
                 strict_slashes=False)
@swag_from('documentation/user_preference/get_users_preferences.yml',
           methods=['GET'])
def get_user_preferences(user_id):
    """
    Retrieves the list of all Preference objects of a User
    """
    user = storage.get(User, user_id)

    if not user:
        abort(404)

    preferences = [preference.to_dict() for preference in user.preferences]
    return jsonify(preferences)


@app_views.route('/users/<user_id>/preferences/<preference_id>',
                 methods=['DELETE'], strict_slashes=False)
@swag_from('documentation/user_preference/delete_user_preferences.yml',
           methods=['DELETE'])
def delete_user_preference(user_id, preference_id):
    """
    Deletes a Preference object of a User
    """
    user = storage.get(User, user_id)

    if not user:
        abort(404)

    preference = storage.get(Preference, preference_id)

    if not preference:
        abort(404)
    
    if preference not in user.preferences:
        abort(404)
    user.preferences.remove(preference)
    user.preference_ids.remove(preference_id)

    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/users/<user_id>/preferences/<preference_id>', methods=['POST'],
                 strict_slashes=False)
@swag_from('documentation/user_preference/post_user_preferences.yml',
           methods=['POST'])
def post_user_preference(user_id, preference_id):
    """
    Link a Preference object to a User
    """
    user = storage.get(User, user_id)

    if not user:
        abort(404)

    preference = storage.get(Preference, preference_id)

    if not preference:
        abort(404)

    if preference in user.preferences:
        return make_response(jsonify(preference.to_dict()), 200)
    else:
        user.preferences.append(preference)

    storage.save()
    return make_response(jsonify(preference.to_dict()), 201)
