users = []
products = []
sales = []

class UserAuth():
    '''model for users'''
    def __init__(self, id, name, email, password, role):
        self.id = id
        self.name = name
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
    def get_mail(self):
        return self.email



class ModelProduct():
    '''model for products'''
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

class ModelSale():
    '''model for sales'''
    def __init__(self, id, saleid, product):
        self.saleId = saleId
        self.userId = userId
        self.product = product
    '''Saves a sale to sale records'''
    def save(self):
        new_sale = {
                    "saleId": self.saleId,
                    "userId": self.userId,
                    "product": self.product
                    }
        sales.append(new_sale)
def collapse():
    users.clear()
    products.clear()
    sales.clear()
