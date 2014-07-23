# __init__.py

import os
from flask import Flask

app = Flask(__name__)

app.config.update(dict(
    DEBUG=True,
    SECRET_KEY='secret',
))

from app import views
