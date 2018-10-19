# Store-Manager-APP
[![Build Status](https://travis-ci.com/Arusey/Store-Manager-APP.svg?branch=bg-fix-travis-bug-161338498)](https://travis-ci.com/Arusey/Store-Manager-APP)
[![Maintainability](https://api.codeclimate.com/v1/badges/46d09c2ea4d6f1184814/maintainability)](https://codeclimate.com/github/Arusey/Store-Manager-APP/maintainability)
[![Coverage Status](https://coveralls.io/repos/github/Arusey/Store-Manager-APP/badge.svg?branch=bg-fix-travis-bug-161338498)](https://coveralls.io/github/Arusey/Store-Manager-APP?branch=bg-fix-travis-bug-161338498)


This is a Store Manager Application
To Run and test this application
Take the following steps:
1. Create a virtual enviroment with the command `$ virtualenv -p python3 env`
2. Activate the virtual enviroment with the command `$ source env/bin/activate`
3. Ensure you have installed GIT
4. Clone the repository i.e `$ git clone https://github.com/Arusey/Store-Manager-APP.git`
5. Install requirements `$ pip install -r requirements.txt`
After completing the following, it is time to run the app
i) To run the tests use `$ pytest -v`
ii) To run the application use `export SECRET_KEY="<your secret key>"`
iii) `flask run`

The following endpoints should be working
1. GET /products	Fetch all products
2. GET /products/	Fetch a single product record
3. GET /sales	Fetch all sale records
4. GET /sales/	Fetch a single sale record
5. POST /products	Create a product
6. POST /sales	Create a sale order
7. POST /auth/signup	Signup a user
8. POST /auth/login	Login a user
