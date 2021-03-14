import os
from dotenv import load_dotenv

load_dotenv()

ENV_NAME = os.getenv("ENV_NAME")
DATABASE_URL = os.getenv("DATABASE_URL")
# DATABASE = {
#     'drivername': 'postgres',
#     'host': 'localhost',
#     'port': 5432,
#     'username': 'postgres',
#     'password': '',
#     'database': 'rates_monitor'
# }