class Config():

    debug = False
    SECRET_KEY = "secretkey"

class Develop(Config):
    """Configuration for the development enviroment"""
    debug = True


class Testing(Config):
    """Configuration for the testing enviroment"""
    WTF_CSRF_ENABLED = False
    debug = True


app_config={
"development": Develop,
"testing": Testing
}
