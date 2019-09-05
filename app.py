from flask import Flask,request,redirect,Response, jsonify
import requests
import json
import os
app = Flask(__name__)
SITE_NAME = {
    '19a':f'http://19a:5000', 
    '19b':f'http://19b:5000',
    '19b2':f'http://19b2:5000'}

print(SITE_NAME)
@app.route('/')
def index():
    return 'Flask is running!'

@app.route('/<path:path>')
def proxy(path):
    version = path.split('/')[0]
    geo_path = '/'.join(path.split('/')[1:])
    site_name = SITE_NAME.get(version)
    args = dict(request.args)
    r = requests.get(f'{site_name}/{geo_path}', params=args)
    return jsonify(r.json())

if __name__ == '__main__':
    app.run(debug = False, host='0.0.0.0', port=8000)
