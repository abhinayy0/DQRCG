import requests
from flask import current_app, request, redirect
from oauthlib.oauth2 import WebApplicationClient
import requests
import json
from flask import Blueprint
auth_bp = Blueprint('simple_page',__name__)

#TODO
# client = WebApplicationClient(current_app.config["GOOGLE_CLIENT_ID"])

def get_google_provider_cfg():
    client = WebApplicationClient(current_app.config["GOOGLE_CLIENT_ID"])

    return requests.get(current_app.config["GOOGLE_DISCOVERY_URL"]).json()

@auth_bp.route("/api/login", methods=["GET", "POST"])
def login():
    client = WebApplicationClient(current_app.config["GOOGLE_CLIENT_ID"])
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]
    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=request.base_url + "/callback",
        scope=["openid", "email", "profile"],
    )
    print(request.base_url + "/callback")

    print(request_uri)
    return redirect(request_uri)

@auth_bp.route("/api/login/callback",methods=["GET", "POST"])
def callback():
    client = WebApplicationClient(current_app.config["GOOGLE_CLIENT_ID"])
    code = request.args.get("code")

    google_provider_cfg = get_google_provider_cfg()
    token_endpoint = google_provider_cfg["token_endpoint"]

    token_url, headers, body = client.prepare_token_request(
    token_endpoint,
    authorization_response=request.url,
    redirect_url=request.base_url,
    code=code
)
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(current_app.config["GOOGLE_CLIENT_ID"], current_app.config["GOOGLE_CLIENT_SECRET"]),
    )

    # Parse the tokens!
    client.parse_request_body_response(json.dumps(token_response.json()))

    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)

    if userinfo_response.json().get("email_verified"):
        unique_id = userinfo_response.json()["sub"]
        users_email = userinfo_response.json()["email"]
        picture = userinfo_response.json()["picture"]
        users_name = userinfo_response.json()["given_name"]

    print(userinfo_response.json())

    return {"message":"Logged in"}