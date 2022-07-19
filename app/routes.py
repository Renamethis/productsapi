from flask import jsonify, abort, request
from .tasks import *
from . import app

@app.route("/imports", methods=["POST"])
def add_user():
    return jsonify({"result": True}), 200