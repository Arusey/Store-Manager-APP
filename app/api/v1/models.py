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
    def __init__(self, data):
        self.id = len(products) + 1
        self.data = data
        
        

    def add_product(self):
        payload = {
        'id' : self.id,
        'name': self.data["name"],
        'category' : self.data["category"],
        'description': self.data["description"],
        'currentstock' : self.data["currentstock"],
        'minimumstock' : self.data["minimumstock"],
        'price': self.data["price"]
        }

        products.append(payload)

class ModelSale():
    '''model for sales'''
    def __init__(self, id, saleId, product):
        self.saleId = saleId
        # self.userId = userId
        self.product = product
    '''Saves a sale to sale records'''
    def save(self):
        new_sale = {
                    "saleId": self.saleId,
                    # "userId": self.userId,
                    "product": self.product
                    }
        sales.append(new_sale)
def collapse():
    users.clear()
    products.clear()
    sales.clear()
