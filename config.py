import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    QR_FOLDER = os.path.join(basedir, "static")