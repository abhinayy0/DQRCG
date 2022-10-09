import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY","Notsecret")
    QR_FOLDER = os.path.join(basedir, "generatedqrs")
    if not os.path.exists(QR_FOLDER):
        os.mkdir(QR_FOLDER)
    DEBUG= os.environ.get("DEBUG", False)

    # Configuration
    GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID", None)
    GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET", None)
    GOOGLE_DISCOVERY_URL = (
        "https://accounts.google.com/.well-known/openid-configuration"
    )