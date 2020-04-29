import sqlite3 as sql
from sqlite3 import Error
from includes.helper import *

# Configuration
config = {
    "database": DATABASE_PATH + "/database.sqlite",
}

# Try to connect to our sqlite db :)
try:
    db = sql.connect(config['database'])
except Error:
    exit("An error occured while trying to connect to DB !")