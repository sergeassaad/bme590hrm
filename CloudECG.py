"""

CloudECG.py:
Web server implementation using Flask. Uses the HRM class for calculations.

routes:

/heart_rate/summary:
    input: time array, voltage array
    output: time array, instantaneous HR array, tachy- and bradycardia annotations

/heart_rate/average:
    input: time array, voltage array, averaging period
    output: averaging period, time array, average HR array, tachy- and bradycardia annotations

/api/requests:
    output: number of requests to server since last reboot
"""

from flask import Flask, request, jsonify
app = Flask(__name__)
req_num = 0


def send_error(message, code):
    err = {
        "error": message
    }
    return jsonify(err), code

@app.route("/heart_rate/summary", methods=['POST'])
def cloud_ecg_summary():
    from HeartRateMonitor import HRM
    global req_num
    req_num += 1
    try:
        obj = HRM(request.json['time'], request.json['voltage'])
    except ValueError:
        return send_error("Improper time & voltage arrays", 400)

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
    global req_num
    req_num += 1
    try:
        obj = HRM(request.json['time'], request.json['voltage'],
              averaging_period = request.json['averaging_period'])
    except ValueError:
        return send_error("Improper time & voltage arrays, averaging period", 400)
    obj.ihr()
    obj.avghr()
    obj.detect_cardia()
    tachycardia = obj.tachy_avg
    bradycardia = obj.brady_avg

    output = {"averaging_period": request.json['averaging_period'],
              "time_interval": request.json['time'],
              "average_heart_rate": obj.avghr_list,
              "tachycardia_annotations": tachycardia,
              "bradycardia_annotations": bradycardia}

    return jsonify(output)


@app.route("/api/requests")
def count_requests():
    return jsonify({"number_of_requests": req_num})
