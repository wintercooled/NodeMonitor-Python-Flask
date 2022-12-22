import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'PLrEWuytn8784nV7Ya5Hn4vR322n7Myx'

    NODE_IP = 'localhost'
    NODE_PORT = '18891'
    RPC_USERNAME = 'user'
    RPC_PASSWORD = 'password'
