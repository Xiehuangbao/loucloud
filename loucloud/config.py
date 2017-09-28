# -*- coding: utf-8 -*-

import os


class DefaultConfig(object):
    PROJECT = "loucloud"

    DEBUG = False

    TESTING = False

    SECRET_KEY = 'your secret key'

    SQLALCHEMY_ECHO = True

    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@192.168.2.122/db?charset=utf8'

    CACHE_TYPE = 'simple'
    CACHE_DEFAULT_TIMEOUT = 60
