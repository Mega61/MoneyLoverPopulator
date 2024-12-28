import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

class Alchemy_engine:

    def create_engine():
        load_dotenv()
        engine = create_engine(os.getenv('SQLALCHEMY_URI'), echo=True)
        return engine
