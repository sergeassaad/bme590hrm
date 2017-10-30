"""
AvgHR.py
========
avghr:

-	Input: Lists of times, list of voltages, lower time bound, upper time bound
-	Output: 1 value for average heart rate for the specified time range
"""

def avghr_unbound(times, voltages):
    SECONDS_PER_MIN = 60.0
    if(len(times)== 0 or len(times) == 1):
        return 0
    print('times0: %f' % times[0])
    print('times1: %f' % times[len(times)-1])
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
    print peak_times
    print peak_count
    if(peak_count ==0):
        return 0
    print('denom: %f' % (peak_times[-1] - peak_times[0]))
    time_range = peak_times[-1] - peak_times[0]

    if(peak_count==1):
        time_range = times[-1]-times[0]
    return SECONDS_PER_MIN* peak_count /time_range


def avghr(times, voltages, t1=0, t2=float('inf')):
    if len(times) == 0 or len(voltages) == 0:
        raise ValueError('Empty arrays!')

    if t1 > t2:
        t1_temp = t1
        t1 = t2
        t2 = t1_temp
    if t1 < times[0]:
        t1 = times[0]
    if t2 > times[len(times) - 1]:
        t2 = times[len(times) - 1]

    times_t1 = [abs(t - t1) for t in times]
    times_t2 = [abs(t - t2) for t in times]

    idx_t1 = times_t1.index(min(times_t1))
    idx_t2 = times_t2.index(min(times_t2))

    times_bound = times[idx_t1:idx_t2 + 1]
    voltages_bound = voltages[idx_t1:idx_t2 + 1]

    return avghr_unbound(times_bound, voltages_bound)

def avghr_period(times, voltages, averaging_period):
    lower_t = times[0]
    avghr_list = []
    while(lower_t<=times[len(times)-1]):
        upper_t = averaging_period + lower_t
        avghr_list.append(avghr(times,voltages,lower_t,upper_t))
        lower_t = lower_t + averaging_period
    return avghr_list