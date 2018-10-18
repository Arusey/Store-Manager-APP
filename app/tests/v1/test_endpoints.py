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
            "password": "kevin",
            "role": "admin"
        })
        admin_signup = self.test_client.post(
            "/storemanager/api/v1/auth/signup",
            data=self.user_admin_details, headers={
                'content-type': 'application/json'})
        self.user_attendant_details = json.dumps({
                "name": "brian",
                "email": "brian@email.com",
                "password": "brian",
                "role": "attendant"
            })
        attendant_signup = self.test_client.post("/storemanager/api/v1/auth/signup",
                                                     data=self.user_attendant_details,
                                                     headers={
                                                        'content-type': 'application/json'
                                                        })
        self.login_admin = json.dumps({
            "email": "kevin@email.com",
            "password": "kevin"
        })
        admin_login = self.test_client.post("/storemanager/api/v1/auth/login",
                                            data=self.login_admin, headers={
                                                'content-type': 'application/json'
                                            })
        self.token_for_admin = json.loads(admin_login.data.decode())["token"]
        self.login_attendant = json.dumps({
            "email": "brian@email.com",
            "password": "brian"
        })
        attendant_login = self.test_client.post("/storemanager/api/v1/auth/login",
                                                data=self.login_attendant,
                                                headers={
                                                    'content-type': 'application/json'
                                                })
        self.token_for_attendant = json.loads(attendant_login.data.decode())["token"]

    def tearDown(self):
        """removes all the context and dicts"""
        collapse()
        # self.app_context.pop()
    def test_signup(self):
        response = self.test_client.post("/storemanager/api/v1/auth/signup",
                                         data=self.user_admin_details,
                                         content_type='application/json')
        self.assertEqual(response.status_code, 201)
    def test_empty_login(self):
        data = json.dumps(
            {
                "email": "",
                "password": ""
            }
        )
        response = self.test_client.post("storemanager/api/v1/auth/login",
                                         data=data,
                                         content_type='application/json')
        self.assertEqual(response.status_code, 401)

    def test_wrong_login(self):
        data = json.dumps({
            "email": "blah@email.com",
            "password": "blahblah"
        })
        response = self.test_client.post("storemanager/api/v1/auth/login",
                                         data=data,
                                         content_type='application/json')

        self.assertEqual(response.status_code, 401)

    def test_login_granted(self):

        response = self.test_client.post("/storemanager/api/v1/auth/login",
                                         data=self.login_admin,
                                         headers={
                                            'content-type': 'application/json'
                                            })
        self.assertEqual(response.status_code, 200)

    def test_post_product(self):
        response = self.test_client.post("storemanager/api/v1/products",
                                         data=json.dumps({
                                            'name': 'minji',
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
