"""InstHR
Module Author: Joseph Cobb
Function: Calculate instantaneous heart rate from EKG
The function takes two input arguments:
    arg1: a time array
    arg2: a voltage array
and outputs:
    output1: time vector of tuples (start,end) in seconds
    output2: heart rate rounded to nearest integer
where the (start,end) indicates the time the heartbeat occurred.
Assume 1000 samples/sec
"""


def ihr(t, v):

    if len(t) != len(v):
        return 'Please input lists with identical lengths.'

    for i in range(len(t)):
        if type(t[i]) not in (int, float) or type(v[i]) not in (int, float):
            return 'Please input a list of times and a list of lead voltages as arguments.'

    times = []
    voltages = []
    heart_rates = []
    max_v = float(max(v))
    min_v = float(min(v))
    threshold_constant = float(0.75)
    threshold = threshold_constant*(max_v - min_v) + min_v

    for i in range(len(v)):
        if v[i] >= threshold and v[i] >= v[i-1] and v[i] > v[i+1]:
            if round(t[i], 3) not in times:
                times.append(round(t[i], 3))
                voltages.append(v[i])

    time_pairs = []

    for i in range(len(times)-1):
        time_pairs.append((times[i], times[i+1]))

    for i in range(len(time_pairs)):
        heart_rates.append(round(60/float(time_pairs[i][1] - time_pairs[i][0])))

    return time_pairs, heart_rates
