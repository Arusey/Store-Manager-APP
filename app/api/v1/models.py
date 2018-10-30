users = []


class UserAuth():
    def __init__(self, name, email, password, role):
        self.name = username
        self.email = email
        self.password = password
        self.role = role

    def save_user(self):
        id = len(users) + 1
        user = {
            'id' : self.id,
            'name' : self.name,
            'email': self.email,
            'password' : self.password,
            'role' : self.role
        }
        users.append(user)

def collapse():
    users = []
