import os

try:
    TOKEN = os.environ["TG_ROBOT_TOKEN"]
    DB_PATH = "/usr/src/app/database"
except KeyError:
    import Config
    TOKEN = Config.token
    DB_PATH = "./"