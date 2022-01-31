from flask import Flask, render_template, request, send_from_directory, redirect
from config import Config
from utils import generate_qrcode
import uuid, os

app = Flask(__name__)
app.config.from_object(Config)

URLS_LIST ={}

@app.get("/")
def home():
    return render_template("home.html")

@app.get("/route/<path:prefix>")
def prefix_reroute(prefix):
    url = URLS_LIST.get(prefix, None)
    if url:
        return redirect(url, code=302)
    return {"message":"Sorry the url does not exist."}

@app.post("/qrcode")
def generate_qr_code():
    user_url = request.form['url']
    random_id = uuid.uuid4().hex
    URLS_LIST[random_id] = user_url
    dynamic_url = request.host_url+ "route/"+ random_id
    filename = generate_qrcode(dynamic_url, random_id)
    filename = random_id+".png"
    return render_template("qr.html",filename= filename, generated_url =dynamic_url )

@app.route('/<path:path>')
def send_qr_image(path):
    return send_from_directory('static',path)

if __name__ == "__main__":
    app.run(debug = True)
