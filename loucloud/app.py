# -*- coding: utf-8 -*-

import os

from flask import Flask, request, render_template
from .config import DefaultConfig
from .extension import db, cache, login_manager
from .user import user

# For import *
__all__ = ['create_app']

DEFAULT_BLUEPRINTS = {
    user,
}


def create_app(config=None, app_name=None, blueprints=None):
    """create a flask app."""

    if app_name is None:
        app_name = DefaultConfig.PROJECT

    if blueprints is None:
        blueprints = DEFAULT_BLUEPRINTS

    app = Flask(app_name)
    configure_app(app, config)
    configure_extension(app)
    configure_blueprint(app, blueprints)

    return app


def configure_app(app, config=None):
    """different ways of configurations."""

    app.config.from_object(DefaultConfig)


def configure_extension(app):
    # flask-sqlalchemy
    db.init_app(app)
    # flask-cache
    cache.init_app(app)
    # flask-login
    # login_manager.login_view = 'user.index'
    # login_manager.setup_app(app)


def configure_blueprint(app, blueprints):
    """configure blueprints in views."""

    for blueprint in blueprints:
        app.register_blueprint(blueprint)
