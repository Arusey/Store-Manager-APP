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

    def tearDown(self):
        """removes all the context and dicts"""
        print(collapse)
        collapse()
        self.app_context.pop()
    def test_signup(self):
        response = self.test_client.post("/storemanager/api/v1/auth/signup",
                                         data=self.user_admin_details,
                                         content_type='application/json')
        self.assertEqual(response.status_code, 201)
