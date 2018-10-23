# Store-Manager-APP
[![Build Status](https://travis-ci.com/Arusey/Store-Manager-APP.svg?branch=bg-fix-travis-bug-161338498)](https://travis-ci.com/Arusey/Store-Manager-APP)
[![Maintainability](https://api.codeclimate.com/v1/badges/46d09c2ea4d6f1184814/maintainability)](https://codeclimate.com/github/Arusey/Store-Manager-APP/maintainability)
[![Coverage Status](https://coveralls.io/repos/github/Arusey/Store-Manager-APP/badge.svg?branch=bg-fix-travis-bug-161338498)](https://coveralls.io/github/Arusey/Store-Manager-APP?branch=bg-fix-travis-bug-161338498)

App Description
===============
This is a store manager application that allows the stakeholders of a given store to perform actions such as:
* Sign up to the application
* Login to the application
* Post a product 
* Post a Sale
* Get all products
* Get single product
* Get all products
* Get all sales
* Get single sale

Installation
============

Take the following steps:
1. Create a virtual enviroment with the command `$ virtualenv -p python3 env`
1. Activate the virtual enviroment with the command `$ source env/bin/activate`
1. Ensure you have installed GIT
1. Clone the repository i.e `$ git clone https://github.com/Arusey/Store-Manager-APP.git`
1. Install requirements `$ pip install -r requirements.txt`

Documentation
=============
https://documenter.getpostman.com/view/4790487/RWgwRFeP

Heroku Deploy
=============
https://storemanagerkevin.herokuapp.com/


Running Tests
=============
After completing the following, it is time to run the app
1. To run the tests use `$ pytest -v`
1. To run the application use `export SECRET_KEY="<your secret key>"`
1. `flask run`

The following endpoints should be working:

|Endpoint|functionality|contraints(requirements)|
|-------|-------------|----------|
|post /api/v1/auth/signup|create a user|user information|
|post /api/v1/auth/login | login |requires authentication |
|get /api/v1/products| get all the products| pass a token |
|get /api/v1/products/<int:id>|return a single product| product id, pass token|
|post /api/v1/products | create a new product entry| product data, pass token|
|post /api/v1/sales | create a new sale| product id, pass token|
|get /api/v1/sales | get all sales entries| pass token|
|get/api/v1/sales/<saleid>|get a single sale entry| sale id, pass token| 
  
 Technologies used include:
 ==========================
 * Python
 * Flask 
 * Flask-Restful
 * Json Web Tokens
 * Heroku
 * Travis CI
 * Coveralls
 * Code Climate
 
 
 
  
  
