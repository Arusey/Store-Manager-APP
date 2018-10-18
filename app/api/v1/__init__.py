from flask import Flask, Blueprint
from flask_restful import Api, Resource
from .views import SignUp, Login, Product, Sale
myblue = Blueprint("api", __name__, url_prefix="/storemanager/api/v1")

api = Api(myblue)
api.add_resource(SignUp, '/auth/signup')
api.add_resource(Login, '/auth/login')
api.add_resource(Product, '/products')
api.add_resource(Sale, '/sales')
