import pathlib

BASE_DIR = pathlib.Path(__file__).parent

config = {
    'database': 'postgres',
    'user': 'postgres',
    'password': '1234',
    'host': 'localhost'
}
