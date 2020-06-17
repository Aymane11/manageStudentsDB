from os.path import dirname, abspath

ROOT = dirname(dirname(abspath(__file__)))

STORAGE_PATH = ROOT + "/storage"

DATABASE_PATH = STORAGE_PATH + "/databases"

DATA_PATH = STORAGE_PATH + "/data"