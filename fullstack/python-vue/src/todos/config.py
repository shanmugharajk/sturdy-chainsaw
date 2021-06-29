from starlette.config import Config

config = Config(".env")

# database
SQLALCHEMY_DATABASE_URI = config("SQLALCHEMY_DATABASE_URI", default=None)
