import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


#postgres://rxxhlhzglhwwpo:bc2a134e64a268bddd42040a0657e986cd02c276e60fcc06850c669d62d0f514@ec2-54-217-221-21.eu-west-1.compute.amazonaws.com:5432/d7b4vbivap2g0c