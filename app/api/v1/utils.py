from flask import jsonify, abort
from validate_email import validate_email
import re

from .models import users

class Validation:
    def validate_user_details(self, data):
        self.name = data["name"]
        self.email = data["email"]
        self.password = data["password"]
        self.role = data["role"]
        valid_mail = validate_email(self.email)
        if not valid_mail:
            Response = "Email not valid"
            abort(406, Response) 
        for user in users:
            if self.email == user["email"]:
                Response = "User Exists"
                abort(405, Response)
        if self.password < 6 or self.password > 20:
            Response = "Should not exceed 20 characters or below 6 characters"
            abort(405, Response)
         

