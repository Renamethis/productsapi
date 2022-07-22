from flask import jsonify, abort, request
from .tasks import *
from . import app

# Unit import endpoint
@app.route("/imports", methods=["POST"])
def imports():
    data = request.json
    task = importNode.delay(data)
    result = task.wait(timeout=None)
    if(result is None):
        abort(400)
    return jsonify(result), 200

# Delete unit endpoint
@app.route("/delete/<uuid>", methods=["DELETE"])
def delete(uuid):
    task = deleteNode.delay(uuid)
    result = task.wait(timeout=None)
    if(result != 200):
        abort(result)
    return jsonify({"result": "Удаление прошло успешно"}), 200

# Get node information endpoint
@app.route("/nodes/<uuid>", methods=["GET"])
def nodes(uuid):
    task = getNode.delay(uuid)
    result = task.wait(timeout=None)
    if(result['code'] != 200):
        abort(result['code'])
    del result['code']
    return jsonify(result), 200

# Get recent units endpoint
@app.route("/sales", methods=["GET"])
def sales():
    task = getSales.delay(request.args.get("date"))
    result = task.wait(timeout=None)
    if(result is None):
        abort(400)
    return jsonify(result), 200

# Get unit statistic endpoint
@app.route("/nodes/<uuid>/statistic", methods=["GET"])
def statistic(uuid):
    task = getNodeStatistics.delay(uuid, request.args.get("dateStart"), request.args.get("dateEnd"))
    result = task.wait(timeout=None)
    if(result["code"] != 200):
        abort(result["code"])
    return jsonify(result["result"]), 200