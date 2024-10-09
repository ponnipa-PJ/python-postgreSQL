import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    if SQLALCHEMY_DATABASE_URI is None:
        print("DATABASE_URL not defined in the .env file.")
    else:
        print(f"Database URL: {SQLALCHEMY_DATABASE_URI}")

