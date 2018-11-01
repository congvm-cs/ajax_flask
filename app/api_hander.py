from flask import Blueprint
from flask import jsonify

send_to_server = Blueprint('send2server', __name__)

@send_to_server.route("/api/pop", methods=['POST'])
def pop():
    data = {
        "data": "this is my data",
        "status": "success"
    }
    return jsonify(data)

