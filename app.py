import os
import flask
import requests
from dotenv import load_dotenv

load_dotenv()

app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template("index.html")

@app.route('/send', methods=["post"])
def send_message():
    text = flask.request.form.get("text", "[EMPTY]")
    token = os.getenv("BOT_TOKEN")
    requests.post(f"https://api.telegram.org/bot{token}/sendMessage", data={
        "chat_id": 2052168739,
        "text": f"""\
New anonymous message ✅

{text}

{flask.request.host_url}
{flask.request.user_agent}
"""
    })
    return flask.redirect('/')