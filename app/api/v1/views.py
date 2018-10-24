from flask import jsonify, make_response, request
from flask_restful import Resource
from functools import wraps
from instance.config import Config
import datetime
import jwt
import json

from .models import UserAuth, users, ModelProduct, products, sales
from .utils import AuthValidate, ProductValidate


def token_required(func):
    '''creates a token'''
    @wraps(func)
    def decorated(*args, **kwargs):
        token = None
        current_user = None
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
        '''endpoint for posting a product'''
        if current_user and current_user["role"] != "admin":
            return make_response(jsonify({
                "Message": "you must be an admin endpoint"}
            ), 403)
        data = request.get_json()
        if not data:
            return make_response(jsonify({
                "Message": "Kindly ensure you have inserted your details"
            }), 400)
        ProductValidate.validate_key_products(self, data)
        id = len(products) + 1
        name = data["name"]
        category = data["category"]
        description = data["description"]
        currentstock = data["currentstock"]
        minimumstock = data["minimumstock"]
        price = data["price"]

        product = ModelProduct(data)
        product.add_product()
        return make_response(jsonify({
            "Status": "ok",
            "Message": "Product posted successfully",
            "Products": products
        }
        ), 201)


    def get(self):
        '''endpoint for getting all products'''
        if len(products) == 0:
            return  make_response(jsonify({
                "Message": "No products have been posted yet"
            }), 404)
        return make_response(jsonify({
            "Status": "ok",
            "Message": "All products fetched successfully",
            "products": products
        }
        ), 200)


class SingleProduct(Resource):
    '''endpoint for getting a single product'''
    @token_required
    def get(current_user, self, id):
        if len(products) == 0:
            return make_response(jsonify(
                {
                    "Message": "No products have been posted yet"
                }
            ), 404)
        for product in products:
            if int(id) == product["id"]:
                return make_response(jsonify({
                    "Status": "ok",
                    "Message": "Product fetched",
                    "Product": product
                }
                ), 200)
        return make_response(jsonify(
            {
                "Message": "The product id given is non-existent"
            }
        ), 404)


class Sale(Resource):
    '''ending for getting all sales'''
    @token_required
    def get(current_user, self):
        if current_user["role"] != "admin":
            return make_response(jsonify(
            {
                "Message": "you are not an admin"
            }
            ), 401)
        if len(sales) == 0:
            return make_response(jsonify({
                "Message": "no sales have been made yet"
            }), 404)


        return make_response(jsonify({
            "Status": "ok",
            "Message": "All products fetched successfully",
            "sales": sales
        }
        ), 200)


    '''Endpoint for posting a sale'''
    @token_required
    def post(current_user, self):
        total = 0
        data = request.get_json()
        # print(data)
        if current_user["role"] != "attendant":
            return make_response(jsonify({
                "Message": "You must be an attendant to access this endpoint"
            }
            ) , 403)
        id = data['id']
        for product in products:
            if product["id"] != id:
                return make_response(jsonify({
                    "Message": "product does not exist"
                                  }), 404)
            if product["currentstock"] > 0:
                if product["id"] == id:
                    sale = {
                        "saleid": len(sales) + 1,
                        "product": product
                    }
                    userId = current_user["id"]
                    product["currentstock"] = product["currentstock"] - 1
                    sales.append(sale)
                    for sale in sales:
                        if product["id"] in sale.values():
                            total = total + int(product["price"])
                    return make_response(jsonify({
                        "Status": "ok",
                        "Message": "sale is successfull",
                        "Sales": sales,
                        "total cost": total
                    }), 201)
                else:
                    return make_response(jsonify({
                        "Status": "non-existent",
                        "Message": "item not found"
                        }), 404)
            else:
                return make_response(jsonify({
                    "Status": "not found",
                    "Message": "items have run out"

                }), 404)


class SingleSale(Resource):
    '''endpoint for getting a single sale'''
    @token_required
    def get(current_user, self, saleid):

        if len(sales) == 0:
            return make_response(jsonify({
                "Message": "No sales have been made yet"
            }), 404)
        for sale in sales:
            if saleid == sale["saleid"]:
                return make_response(jsonify({
                    "Status": "Sale found",
                    "Message": "Single sale retrieved",
                    "Sale": saleid
                }
                ), 200)


class SignUp(Resource):
    '''endpoint for signing up a user'''
    def post(self):
        data = request.get_json()

        if not data:
            return make_response(jsonify(
            {
                "Message": "Please enter details"
            }
            ), 400)
        AuthValidate.validate_key_name(self, data)
        AuthValidate.validate_empty_data(self, data)
        AuthValidate.validate_data(self, data)
        AuthValidate.validate_details(self, data)
        id = len(users) + 1
        name = data["name"]
        email = data["email"]
        password = data["password"]
        role = data["role"]
        user = UserAuth(id, name, email, password, role)
        user.save_user()
        return make_response(jsonify({
            "Status": "ok",
            "Message": "user successfully created",
            "user": user.get_mail() + " registration successful"}), 201)


class Login(Resource):
    '''endpoint for logging in a user'''
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
