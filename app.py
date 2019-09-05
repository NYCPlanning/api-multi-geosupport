from flask import Flask, request, jsonify
import requests
import json
import os
app = Flask(__name__)

print(SITE_NAME)
@app.route('/')
def index():
    return 'Flask is running!'

@app.route('/<path:path>')
def proxy(path):
    version = path.split('/')[0]
    geo_path = '/'.join(path.split('/')[1:])
    args = dict(request.args)
    r = requests.get(f'http://{version}:5000/{geo_path}', params=args)
    return jsonify(r.json())

if __name__ == '__main__':
    app.run(debug = False, host='0.0.0.0', port=8000)
