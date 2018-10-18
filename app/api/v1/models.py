users = []
products = []

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

class PostProduct():
    def __init__(self, id, name, category, desc, currstock, minstock, price):
        self.id = id
        self.name = name
        self.category = category
        self.desc = desc
        self.currstock = currstock
        self.minstock = minstock
        self.price = price

    def add_product(self):
        payload = {
        'id' : self.id,
        'name': self.name,
        'category' : self.category,
        'desc': self.desc,
        'currstock' : self.currstock,
        'minstock' : self.minstock,
        'price': self.price
        }

        products.append(payload)
        print(products)

def collapse():
    users = []
