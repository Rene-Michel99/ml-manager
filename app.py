import os
from flask_api import create_app
from flask_api.config.config import config_dict


ENVIRONMENT = os.getenv("ENVIRONMENT")

if ENVIRONMENT == "dev":
    app = create_app(config=config_dict["dev"])

elif ENVIRONMENT == "production":
    app = create_app(config=config_dict["production"])

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
