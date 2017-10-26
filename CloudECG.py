""" Put Sphinx friendly docstring
"""
from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route("/heart_rate/summary", methods=['POST'])
def cloud_ecg_summary():
    from HeartRateMonitor import HRM

    obj = HRM(request.json['time'], request.json['voltage'])
    instant_hr = obj.ihr()[1]
    tachycardia, bradycardia = obj.detect_cardia()

    output = {"time": obj.times, "instantaneous_heart_rate": instant_hr,
              "tachycardia_annotations": tachycardia,
              "bradycardia_annotations": bradycardia}

    return jsonify(output)


@app.route("/heart_rate/average", methods=['POST'])
def cloud_ecg_average():
    from HeartRateMonitor import HRM

    obj = HRM(request.json['time'], request.json['voltage'])
    obj.ihr()
    obj.avghr()
    tachycardia, bradycardia = obj.detect_cardia()

    output = {"averaging_period": ,"time_interval": , "average_heart_rate": ,
              "tachycardia_annotations": tachycardia,
              "bradycardia_annotations": bradycardia}

    return jsonify(output)
