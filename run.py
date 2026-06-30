#!/usr/bin/env python3

import os
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask

from app import models
# Import the utility to get the correct database path
from app.models import get_database_path
from extensions import Base, db

# We import the models here so SQLAlchemy "registers" them
# before db.create_all() is called.


# 12-Factor apps keep settings in environment variables.
# In local development, python-dotenv reads those values from .env.
# On a hosting service, the platform provides real environment variables.
load_dotenv()

app = Flask(__name__)

environment = os.getenv("FLASK_ENV", "production").lower()
debug_mode = os.getenv("FLASK_DEBUG", "false").lower() in ["true", "1", "yes"]
secret_key = os.getenv("SECRET_KEY")

# A fallback secret is okay for students running locally, but production must
# provide a real SECRET_KEY so cookies and sessions are not easy to forge.
if not secret_key:
    if environment == "development":
        secret_key = "dev-key-change-me"
    else:
        raise RuntimeError("SECRET_KEY must be set in the environment.")

app.config["SECRET_KEY"] = secret_key

# DB setup
db_path = get_database_path()
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db.init_app(app)

with app.app_context():
    db.create_all()

# Import routes after app is created to avoid circular imports
from flask_app import *

if __name__ == "__main__":
    # PORT lets a hosting platform choose where the web process listens.
    # Locally, it still defaults to the familiar http://localhost:5000.
    port = int(os.getenv("PORT", "5000"))
    host = os.getenv("HOST", "127.0.0.1")
    app.run(host=host, port=port, debug=debug_mode)
