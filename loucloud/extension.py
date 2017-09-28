# -*- coding: utf-8 -*-

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from flask_cache import Cache

cache = Cache()

from flask_login import LoginManager

login_manager = LoginManager()
