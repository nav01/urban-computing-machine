from flask import Flask
from flask import request, url_for
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
    return requests.get(
        SNIPE_IT_BASE_API_URL + url_for('get_asset_by_tag', asset_tag=asset_tag), 
        headers=SNIPE_IT_REQUEST_HEADERS
    ).json()

@app.route("/users")
def get_users():
    params = {'limit': 10, 'offset': 0, 'search': request.args.get('search')}
    return requests.get(
        SNIPE_IT_BASE_API_URL + url_for('get_users'), 
        headers=SNIPE_IT_REQUEST_HEADERS, 
        params=params
    ).json()
    
@app.route("/users/<user_id>/assets")
def get_users_assets(user_id):
    return requests.get(
        SNIPE_IT_BASE_API_URL + url_for('get_users_assets', user_id=user_id),
        headers=SNIPE_IT_REQUEST_HEADERS
    ).json()
    
@app.route("/users/<user_id>", methods=['PATCH'])
def patch_users(user_id):
    return requests.patch(
        SNIPE_IT_BASE_API_URL + url_for('patch_users', user_id=user_id),
        headers=SNIPE_IT_REQUEST_HEADERS,
        json=request.json
    ).json()
    
@app.route("/statuslabels")
def get_status_labels():
    return requests.get(
        SNIPE_IT_BASE_API_URL + url_for('get_status_labels'),
        headers=SNIPE_IT_REQUEST_HEADERS
    ).json()
    
@app.route("/hardware/<asset_id>/checkout", methods=['POST'])
def checkout_asset(asset_id):
    return requests.post(
        SNIPE_IT_BASE_API_URL + url_for('checkout_asset', asset_id=asset_id),
        headers=SNIPE_IT_REQUEST_HEADERS,
        json=request.json
    ).json()
    
@app.route("/hardware/<asset_id>/checkin", methods=['POST'])
def checkin_asset(asset_id):
    if request.data:
        return requests.post(
            SNIPE_IT_BASE_API_URL + url_for('checkin_asset', asset_id=asset_id),
            headers=SNIPE_IT_REQUEST_HEADERS,
            json=request.json
        ).json()
    else:
        return requests.post(
            SNIPE_IT_BASE_API_URL + url_for('checkin_asset', asset_id=asset_id),
            headers=SNIPE_IT_REQUEST_HEADERS,
        ).json()
