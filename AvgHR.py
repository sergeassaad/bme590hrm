"""
AvgHR.py
========
avghr:

-	Input: Lists of times, list of voltages, lower time bound, upper time bound
-	Output: 1 value for average heart rate for the specified time range
"""


def avghr_unbound(times, voltages):
    dt = times[1] - times[0]  # assume constant sampling rate
    threshold_constant = 0.7
    voltage_range = max(voltages) - min(voltages)
    threshold = threshold_constant * voltage_range + min(voltages)
    peak_count = 0
    peak_times = []

    for i in range(0, len(voltages) - 1):
        if (voltages[i] >= voltages[i - 1] and voltages[i] > voltages[i + 1])\
                and voltages[i] > threshold:
            peak_count += 1
            peak_times.append(times[i])

    return 60.0 * peak_count / (peak_times[-1] - peak_times[0])


def avghr(times, voltages, t1=0, t2=float('inf')):
    if t1 < times[0]:
        t1 = times[0]
    if t2 > times[len(times) - 1]:
        t2 = times[len(times) - 1]
    if t1 > t2:
        t1_temp = t1
        t1 = t2
        t2 = t1_temp

    times_t1 = [abs(t - t1) for t in times]
    times_t2 = [abs(t - t2) for t in times]

    idx_t1 = times_t1.index(min(times_t1))
    idx_t2 = times_t2.index(min(times_t2))

    times_bound = times[idx_t1:idx_t2 + 1]
    voltages_bound = voltages[idx_t1:idx_t2 + 1]

    return avghr_unbound(times_bound, voltages_bound)
