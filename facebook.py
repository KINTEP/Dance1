import os
from flask import Flask, redirect, url_for
from flask_dance.contrib.facebook import make_facebook_blueprint, facebook

app = Flask(__name__)
app.secret_key = "FLASK_SECRET_KEY"
app.config["FACEBOOK_OAUTH_CLIENT_ID"] = "663729490855447"
app.config["FACEBOOK_OAUTH_CLIENT_SECRET"] = "aefe081cf32ab312dd3a637b2bac4b83"
facebook_bp = make_facebook_blueprint()
app.register_blueprint(facebook_bp, url_prefix="/login")

@app.route("/")
def index():
    if not facebook.authorized:
        return redirect(url_for("facebook.login"))
    resp = facebook.get("/me")
    assert resp.ok, resp.text
    return "You are {name} on Facebook".format(name=resp.json()["name"])

if __name__ == '__main__':
	app.run(debug = True)