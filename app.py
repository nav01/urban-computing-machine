from flask import Flask
import os
import requests

app = Flask(__name__)
SNIPE_IT_KEY = os.environ.get('SNIPE_IT_KEY')
SNIPE_IT_BASE_API_URL = os.environ.get('SNIPE_IT_BASE_API_URL')

SNIPE_IT_REQUEST_HEADERS = {
    'Authorization': ('Bearer ' + SNIPE_IT_KEY),
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

@app.route("/hardware/bytag/<asset_tag>")
def get_asset_by_tag(asset_tag):
    return requests.get(SNIPE_IT_BASE_API_URL + f'/hardware/bytag/{asset_tag}', headers=SNIPE_IT_REQUEST_HEADERS).json()