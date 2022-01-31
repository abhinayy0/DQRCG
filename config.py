import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = "Notsecret"
    QR_FOLDER = os.path.join(basedir, "generatedqrs")
    DEBUG= True