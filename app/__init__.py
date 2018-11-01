from flask import Flask
from flask import jsonify
from flask import Blueprint
from .api_hander import send_to_server

app = Flask(__name__)
app.register_blueprint(send_to_server)


