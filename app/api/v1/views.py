from flask import jsonify, make_response, request
from flask_restful import Resource
from functools import wraps
from instance.config import Config
import datetime
import jwt
import json

from .models import *

def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return make_response(jsonify({
                                 "Message": "the access token is missing, Login"}, 401))
        try:
            data = jwt.decode(token, Config.SECRET_KEY)
            for user in users:
                if user['email'] == data['email']:
                    current_user = user

        except:

            print(Config.SECRET_KEY)
            return make_response(jsonify({
                "Message": "This token is invalid"
            }, 403))

        return func(current_user, *args, **kwargs)
    return decorated

class Product(Resource):
    @token_required
    def post(current_user, self):
        if current_user["role"] != "admin":
            return make_response(jsonify({
                "Message": "you have no clearance for this endpoint"}
            ), 403)
        id = len(products) + 1
        data = request.get_json()
        name = data["name"]
        category = data["category"]
        desc = data["desc"]
        currstock = data["currstock"]
        minstock = data["minstock"]
        price = data["price"]

        prod = PostProduct(id, name, category, desc, currstock, minstock, price)
        prod.add_product()
        return make_response(jsonify({
            "Status": "ok",
            "Message": "Product posted successfully",
            "Products": products
        }
        ), 201)

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

class Login(Resource):
    def post(self):
        data = request.get_json()
        if not data:
            return make_response(jsonify({
                "Message": "Ensure you have inserted your credentials"
            }
            ), 401)
        email = data["email"]
        password = data["password"]

        for user in users:
            if email == user["email"] and password == user["password"]:
                token = jwt.encode({
                    "email": email,
                    "exp": datetime.datetime.utcnow() + datetime.timedelta
                                  (minutes=5)
                }, Config.SECRET_KEY)
                return make_response(jsonify({
						     "token": token.decode("UTF-8")}), 200)
        return make_response(jsonify({
            "Message": "Login failed, wrong entries"
        }
        ), 401)
