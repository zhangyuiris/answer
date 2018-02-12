#encoding: utf-8
import os

DEBUG = True

SECRET_KEY = os.urandom(24)

#加上Pymysql的引擎
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:admin@127.0.0.1:3300/answer'
SQLALCHEMY_TRACK_MODIFICATIONS = True


