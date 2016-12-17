from flask import Flask, request, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
import random
import string

def random_string():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(32))

class Config:
    SECRET_KEY = random_string()
    BASE_API_URL = "http://api.beta.dev.careerdream.org/core/v1/"

    @staticmethod
    def init_app(app):
        pass

class ProductionConfig(Config):
    DEBUG = True
    MYSQL_USER = "root"
    MYSQL_PASS = "123456"
    MYSQL_HOST = "127.0.0.1"
    MYSQL_PORT = "3306"
    MYSQL_DB = "psms"

config = {
    "default": ProductionConfig
}