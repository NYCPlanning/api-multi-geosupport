from flask import Flask,request,redirect,Response, jsonify
import requests
import json
app = Flask(__name__)
SITE_NAME = {
    '19a':'http://localhost:5000', 
    '18d':'http://localhost:5001',
    '18c':'http://localhost:5002'}

@app.route('/')
def index():
    return 'Flask is running!'

@app.route('/<path:path>')
def proxy(path):
    version = path.split('/')[0]
    geo_path = ''.join(path.split('/')[1:])
    try: 
        site_name = SITE_NAME.get(version)
        args = dict(request.args)
        r = requests.get(f'{site_name}/{geo_path}', params=args)
        return jsonify(r.json())
    except: 
        return jsonify(f'{version} is not included yet')


if __name__ == '__main__':
    app.run(debug = True, port=5001)
