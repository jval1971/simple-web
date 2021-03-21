from flask import Flask
import requests

app = Flask(__name__)


@app.route('/')
def hello():
    r = requests.get("http://api:6000")
    date = r.headers.get("Api-datetime")
    return f'<html><head><title>Simple wep api</title><body><h1>Date and time</h1><h2>{date}</h2></body></html>'


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
