from flask import jsonify, make_response, request
from flask_restful import Resource
from functools import wraps
from instance.config import Config
import datetime
import jwt
import json

from .models import *


class SignUp(Resource):
    def post(self):
        data = request.get_json()
        id = len(users) + 1
        name = data["name"]
        email = data["email"]
        password = data["password"]
        role = data["role"]

        user = {
            "id": id,
            "name": name,
            "email": email,
            "password": password,
            "role": role
        }
        users.append(user)
        return make_response(jsonify({
            "Status": "ok",
            "Message": "user successfully created",
            "user": users
        }
        ), 201)
