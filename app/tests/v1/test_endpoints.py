
import unittest
import json
from app import create_app
from instance.config import app_config
from app.api.v1.models import collapse


class TestEndpoints(unittest.TestCase):
    """docstring for setting up testEndpoints."""
    def setUp(self):
        self.app = create_app(app_config['testing'])
        self.test_client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.user_admin_details = json.dumps({
            "name": "kevin",
            "email": "kevin@email.com",
            "password": "Kevin@463",
            "role": "admin"
        })
        self.login_admin = json.dumps({
            "email": "kevin@email.com",
            "password": "Kevin@463"
        })
        admin_signup = self.test_client.post(
            "/api/v1/auth/signup",
            data=self.user_admin_details, headers={
                'content-type': 'application/json'})
        print(admin_signup)
        admin_login = self.test_client.post("/api/v1/auth/login",
                                            data=self.login_admin, headers={
                                                'content-type': 'application/json'
                                            })
        print(admin_login.data)
        self.token_for_admin = json.loads(admin_login.data.decode())["token"]
        self.user_attendant_details = json.dumps({
            "name": "brian",
            "email": "brian@email.com",
            "password": "Brian@555",
            "role": "attendant"
        })
        self.login_attendant = json.dumps({
            "email": "brian@email.com",
            "password": "Brian@555"
        })
        attendant_signup = self.test_client.post("/api/v1/auth/signup",
                                                 data=self.user_attendant_details,
                                                 headers={
                                                    'content-type': 'application/json'
                                                    })
        attendant_login = self.test_client.post("/api/v1/auth/login",
                                                data=self.login_attendant,
                                                headers={
                                                    'content-type': 'application/json'
                                                })
        self.token_for_attendant = json.loads(attendant_login.data.decode())["token"]

        self.post_products = json.dumps({
            "name": "minji",
            "category": "food",
            "desc": "great food",
            "currstock": 20,
            "minstock": 2,
            "price": 30
        })
        self.create_sale = json.dumps({
            "id": 1
        })
        self.test_client.post("/api/v1/products",
                              data=json.dumps({
                                    'name': 'minji',
                                    'category': 'food',
                                    'desc': 'great food',
                                    'currstock': 200,
                                    'minstock': 20,
                                    'price': 30
                                    }
                                        ),
                              headers={
                                    'content-type': 'application/json',
                                    "x-access-token": self.token_for_admin
                                })
        self.test_client.post("/api/v1/sales",
                              data=json.dumps({
                                "id": 1
                              }
                              ),
                              headers={
                                'content-type': 'application/json',
                                "x-access-token": self.token_for_attendant
                              })
        self.app_context.push()

    def tearDown(self):
        """removes all the context and dicts"""
        collapse()
        # self.app_context.pop()

    def test_signup(self):
        '''test our sign up endpoint'''
        data= json.dumps(
        {
            "name": "Faith",
            "email": "faith@email.com",
            "password": "Faith@69",
            "role": "attendant"
        }
        )
        response = self.test_client.post("/api/v1/auth/signup",
                                         data=data,
                                         content_type='application/json')
        self.assertEqual(response.status_code, 201)
    def test_empty_signup(self):
        '''test whether user has not inserted details'''
        data = json.dumps(
            {
            "name": "",
            "email": "",
            "password": "",
            "role": ""
            }
        )
        response = self.test_client.post("/api/v1/auth/signup",
                                         data=data,
                                         content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_empty_login(self):
        '''test whether user has not inserted credentials'''
        data = json.dumps(
            {
                "email": "",
                "password": ""
            }
        )
        response = self.test_client.post("/api/v1/auth/login",
                                         data=data,
                                         content_type='application/json')
        self.assertEqual(response.status_code, 401)


    def test_wrong_login(self):
        '''test whether user has inset wrong credentials'''
        data = json.dumps({
            "email": "blah@email.com",
            "password": "blahblah"
        })
        response = self.test_client.post("/api/v1/auth/login",
                                         data=data,
                                         content_type='application/json')

        self.assertEqual(response.status_code, 401)

    def test_login_granted(self):
        '''test whether user hass been succefully'''
        response = self.test_client.post("/api/v1/auth/login",
                                         data=self.login_admin,
                                         headers={
                                            'content-type': 'application/json'
                                            })
        self.assertEqual(response.status_code, 200)

    def test_post_product(self):
        '''test whether a product has been posted'''
        response = self.test_client.post("/api/v1/products",
                                         data=json.dumps({
                                            'name': 'Madondo',
                                            'category': 'food',
                                            'desc': 'great food',
                                            'currstock': 200,
                                            'minstock': 20,
                                            'price': 30
                                            }),
                                         headers={
                                            'content-type': 'application/json',
                                            "x-access-token": self.token_for_admin
                                            })
        self.assertEqual(response.status_code, 201)


    def test_get_all_products(self):
        '''test for getting all products'''
        response = self.test_client.get("/api/v1/products")
        self.assertEqual(response.status_code, 200)
    #

    def test_get_all_sales(self):
        '''test for getting all sales'''
        response = self.test_client.get("/api/v1/sales")
        self.assertEqual(response.status_code, 200)
    #

    def test_post_sale(self):
        '''test for posting a sale'''
        data = json.dumps({
            "id": 1
            })
        response = self.test_client.post("/api/v1/sales",
                                         data=data, headers={
                                             'content-type': 'application/json',
                                             'x-access-token': self.token_for_attendant
                                             })
        self.assertEqual(response.status_code, 201)

    def test_get_single_product(self):
        '''test for getting a single product'''
        response = self.test_client.get("/api/v1/products/1")
        self.assertEqual(response.status_code, 200)

    def test_get_single_sale(self):
        '''test for getting a single sale'''
        response = self.test_client.get("/api/v1/sales/1")
        self.assertEqual(response.status_code, 200)
    def test_existing_user(self):
        '''test for whether a user exists'''
        data = json.dumps({
                "name": "kevin",
                "email": "kevin@email.com",
                "password": "Kevin@463",
                "role": "admin"
        })
        response = self.test_client.post("api/v1/auth/signup",
                                         data=data,
                                         headers={
                                         'content_type': 'application/json'
                                         })
        self.assertEqual(response.status_code, 400)
    def test_password_length(self):
        '''test for password length'''
        data = json.dumps({
                "name": "kevin",
                "email": "kevin@email.com",
                "password": "Kevin@463923748237423",
                "role": "admin"
        })
        response = self.test_client.post("api/v1/auth/signup",
                                         data=data,
                                         headers={
                                         'content_type': 'application/json'
                                         })
        self.assertEqual(response.status_code, 400)
    def test_pass_charisdigit(self):
        '''test for whether a character is a digit'''
        data = json.dumps({
                "name": "kevin",
                "email": "kevin@email.com",
                "password": "Kevin",
                "role": "admin"
        })
        response = self.test_client.post("api/v1/auth/signup",
                                         data=data,
                                         headers={
                                         'content_type': 'application/json'
                                         })
        self.assertEqual(response.status_code, 400)
    def test_pass_char_isupper(self):
        '''test whether password has an uppercase'''
        data = json.dumps({
                "name": "kevin",
                "email": "kevin@email.com",
                "password": "kevin",
                "role": "admin"
        })
        response = self.test_client.post("api/v1/auth/signup",
                                         data=data,
                                         headers={
                                         'content_type': 'application/json'
                                         })
        self.assertEqual(response.status_code, 400)
    def test_pass_char_islower(self):
        '''test whether password has a lowercase'''
        data = json.dumps({
                "name": "kevin",
                "email": "kevin@email.com",
                "password": "KEVIN",
                "role": "admin"
        })
        response = self.test_client.post("api/v1/auth/signup",
                                         data=data,
                                         headers={
                                         'content_type': 'application/json'
                                         })
        self.assertEqual(response.status_code, 400)
    def test_pass_has_special_character(self):
        '''test whether password has an special charater'''
        data = json.dumps({
                "name": "kevin",
                "email": "kevin@email.com",
                "password": "kevin",
                "role": "admin"
        })
        response = self.test_client.post("api/v1/auth/signup",
                                         data=data,
                                         headers={
                                         'content_type': 'application/json'
                                         })
        self.assertEqual(response.status_code, 400)

    def test_data_type(self):
        '''test for a correct data type'''
        data = json.dumps({
                "name": 23409,
                "email": 36482,
                "password": 7348974,
                "role": 93427
        })
        response = self.test_client.post("api/v1/auth/signup",
                                         data=data,
                                         headers={
                                         'content_type': 'application/json'
                                                })
        self.assertEqual(response.status_code, 400)
    def test_product_exists(self):
        '''test whether a product already exists'''
        data = json.dumps({
                'name': 'minji',
                'category': 'food',
                'desc': 'great food',
                'currstock': 200,
                'minstock': 20,
                'price': 30
        })
        response = self.test_client.post("api/v1/auth/products",
                                         data=data,
                                         headers={
                                        'content_type': 'application/json',
                                        'x-access-token': self.token_for_admin
                                         })
        self.assertEqual(response.status_code, 404)
    def test_empty_products(self):
        '''test whether product details are empty'''
        data = json.dumps({
                'name': "",
                'category': "food",
                'desc': "",
                'currstock': "",
                'minstock': "",
                'price': ""
        })
        response = self.test_client.post("api/v1/auth/products",
                                         data=data,
                                         headers={
                                        'content_type': 'application/json',
                                        'x-access-token': self.token_for_admin
                                         })
        self.assertEqual(response.status_code, 404)
