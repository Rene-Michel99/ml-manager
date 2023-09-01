import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    """Define a secret key to application"""

    SECRET_KEY = os.getenv("secret_key", "m3du54as")


class DevConfig(Config):
    """Developer application URL config"""

    URL = "http://localhost:5000/"
    DEBUG = True


class ProdConfig(Config):
    """Production application URL config"""

    URL = 'https://'
    DEBUG = False


config_dict = {"dev": DevConfig, "production": ProdConfig}
