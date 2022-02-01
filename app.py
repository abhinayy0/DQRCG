from flask import Flask, request, send_from_directory, redirect
from config import Config
from utils import generate_qrcode
import uuid, os, requests
from requests.exceptions import ConnectionError
from flask_cors import CORS

app = Flask(__name__, static_folder='dqrcg/client/build', static_url_path='/')
CORS(app)
app.config.from_object(Config)

URLS_LIST ={}

@app.route('/')
def index():
    return {"message":"DQRCG API"}

@app.route('/api/')
def home():
    return {"message":"DQRCG API"}

@app.route('/api')
def homepage():
    return {"message":"DQRCG API"}

@app.get("/route/<path:prefix>")
def prefix_reroute(prefix):
    url = URLS_LIST.get(prefix, None)
    if url:
        return redirect(url, code=302)
    return {"message":"Sorry the url does not exist."}

@app.post("/api/qrcode")
def generate_qr_code():
  
    user_url = request.get_json().get("url")
    try:
        requests.get(user_url)
    except ConnectionError:
        return {"error":"Could not connect to the provided url. Make sure it's reachable."}, 400
    except Exception as e:
        return {"error":f"{e}"}, 400
     
    random_id = uuid.uuid4().hex
    for id, url in URLS_LIST.items():
        if url == user_url:
            random_id = id
            break
    URLS_LIST[random_id] = user_url
    dynamic_url = request.host_url+ "route/"+ random_id
    filename = generate_qrcode(dynamic_url, random_id)
    filename =  request.host_url+"api/"+random_id+".png"
    return {"qrimage": filename, "dynamicurl": dynamic_url}


@app.route('/api/<path:path>')
def send_qr_image(path):
    return send_from_directory(app.config["QR_FOLDER"],path)

