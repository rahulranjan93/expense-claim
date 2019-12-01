import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


#postgres://apjqozxibijqqi:aab97b6b6e0393f57d08dbb5ff8194a303dccd0f0b87c9e279d7b1862049588e@ec2-46-137-120-243.eu-west-1.compute.amazonaws.com:5432/dci9qlsvmg6vpn