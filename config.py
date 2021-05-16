import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', f"sqlite:///{BASE_DIR / 'app.db'}")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ENVIAME_API_BASE_URL = os.getenv('ENVIAME_API_BASE_URL')
    ENVIAME_API_KEY = os.getenv('ENVIAME_API_KEY')
