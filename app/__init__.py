from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from redis import Redis
from dotenv import load_dotenv
import os

# Initialize extensions
db = SQLAlchemy()
r = None

def create_app():
    # Load environment variables from .env
    load_dotenv()

    # Read database config from environment
    DB_USER = os.getenv('DB_USER')
    DB_PASS = os.getenv('DB_PASS')
    DB_NAME = os.getenv('DB_NAME')
    DB_HOST = os.getenv('DB_HOST')
    DB_PORT = os.getenv('DB_PORT')
    REDIS_URL = os.getenv('REDIS_URL')

    # Log the loaded values
    print("🔐 ENV Loaded:")
    print(f"🔗 DB_USER: {DB_USER}")
    print(f"🔗 DB_NAME: {DB_NAME}")
    print(f"🔗 DB_PASS: {DB_PASS}")
    print(f"🔗 REDIS_URL: {REDIS_URL}")

    # Build SQLAlchemy DB URI
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    print(f"✅ SQLAlchemy URI: {SQLALCHEMY_DATABASE_URI}")

    # Flask App Instance
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = True  # Enable query logging

    # Init DB
    db.init_app(app)

    # Init Redis
    global r
    r = Redis.from_url(REDIS_URL)

    # Register Blueprints
    from app.routes import main
    app.register_blueprint(main)

    return app
