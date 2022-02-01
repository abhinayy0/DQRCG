import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY","Notsecret")
    QR_FOLDER = os.path.join(basedir, "generatedqrs")
    if not os.path.exists(QR_FOLDER):
        os.mkdir(QR_FOLDER)
    DEBUG= os.environ.get("DEBUG", False)