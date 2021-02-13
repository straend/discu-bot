import os

DB_URL = os.environ.get('DB_PATH', 'postgresql+psycopg2://postgres:postgres@localhost')
FRONT_BASE = os.environ.get('FRONT_ADDRESS', 'http://localhost:4200')

    