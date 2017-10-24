""" Put Sphinx friendly docstring
"""
from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route("/heart_rate/summary", methods=['POST'])
def cloud_ecg_summary():
    from HeartRateMonitor import HRM

    obj = HRM(request.json['time'], request.json['voltage'])
    obj.ihr()
    obj.detect_cardia()
    
    return


@app.route("/heart_rate/average", methods=['POST'])
def cloud_ecg_average():
    from HeartRateMonitor import HRM

    obj = HRM(request.json['time'], request.json['voltage'])
    obj.ihr()
    obj.avghr()
    obj.detect_cardia()

    return
