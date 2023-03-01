from flask import Flask, Response, Request
from requests import get
from urllib.parse import unquote

import config
import server

app = Flask(__name__)


@app.route('/', methods=['GET'])
def default_index():
    """Default route for requests"""
    return Response('{"status": "400", "message": "Bad request."}', status=400, mimetype="application/json")

@app.route('/status', methods=['GET'])
def status():
    """Returns a simple status overview of the service"""
    response = Response('{"status": "200", "message": "OK!"}', status=200, mimetype="application/json")
    # do more stuff here to validate service status
    return response

@app.route('/addURL', methods=['GET'])
def add_url():
    response = Response('{"status": "501", "message": "Not implemented (Yet!)"}', status=501, mimetype="application/json")
    return response

@app.route('/getURL', methods=['GET'])
def get_url():
    response = Response('{"status": "501", "message": "Not implemented (Yet!)"}', status=501, mimetype="application/json")
    return response

@app.route('/', defaults={'u_path': ''})
@app.route('/<path:u_path>')
def catch_all(u_path):
  response = Response('{"status": "404", "message": "Not found"}', status=404, mimetype="application/json")
  return response

def main():
    """Entry Point"""
    app.run(host='127.0.0.1', port=8080)

if __name__ == '__main__':
    main()