import os
from dotenv import load_dotenv

load_dotenv()
class Config:
    TEST = os.getenv('MONGO_URL')
    MONGO_URL = os.getenv('MONGO_URL')

print("MONGO:", Config.MONGO_URL)
