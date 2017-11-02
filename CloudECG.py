""" Put Sphinx friendly docstring
"""
from flask import Flask, request, jsonify
app = Flask(__name__)
global req_num
req_num = 0

@app.route("/heart_rate/summary", methods=['POST'])
def cloud_ecg_summary():
    from HeartRateMonitor import HRM
    req_num += 1
    obj = HRM(request.json['time'], request.json['voltage'])
    instant_hr = obj.ihr()
    obj.avghr()
    obj.detect_cardia()
    tachycardia = obj.tachy_inst
    bradycardia = obj.brady_inst

    output = {"time": obj.times, "instantaneous_heart_rate": instant_hr,
              "tachycardia_annotations": tachycardia,
              "bradycardia_annotations": bradycardia}

    return jsonify(output)


@app.route("/heart_rate/average", methods=['POST'])
def cloud_ecg_average():
    from HeartRateMonitor import HRM
    req_num += 1
    obj = HRM(request.json['time'], request.json['voltage'],averaging_period = request.json['averaging_period'])
    obj.ihr()
    obj.avghr()
    obj.detect_cardia()
    tachycardia = obj.tachy_avg
    bradycardia = obj.brady_avg

    output = {"averaging_period": request.json['averaging_period'],"time_interval": request.json['time'] , "average_heart_rate": obj.avghr_list,
              "tachycardia_annotations": tachycardia,
              "bradycardia_annotations": bradycardia}

    return jsonify(output)

@app.route("/api/requests")
def count_requests():
    return jsonify({"number_of_requests": req_num})
