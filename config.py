import os
from dotenv import load_dotenv
load_dotenv()
class Config:
    DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///vidshare_default.db')
    SECRET_KEY = os.getenv('SECRET_KEY', 'a_default_secret_key')
    DEBUG = os.getenv('DEBUG', 'False').lower() in ['true', '1', 't', 'y', 'yes']