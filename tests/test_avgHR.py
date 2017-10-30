import os
import sys
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from ReadCSV import readcsv
from AvgHR import avghr
from HeartRateMonitor import HRM


def test_avghr():
    hrlist = [48, 96, 144]
    for i in range(1,len(hrlist)):
        filename = 'ECG_dummy_data_%d_avgHR.csv' % i
        mylist = readcsv(filename)
        times = mylist[0]
        voltages = mylist[1]

        myHRM = HRM(times,voltages)
        assert (abs(myHRM.avghr() - hrlist[i - 1]) < 5)
        lower_bound = times[0] + 0.5 * (times[len(times) - 1] - times[0])
        assert abs(avghr(times, voltages, lower_bound, times[len(times) - 1]) - hrlist[i-1]) < 5


def test_avghr_period():
    import math
    averaging_period = 2
    hrlist_values = 48

    filename = 'ECG_dummy_data_1_avgHR.csv'
    mylist = readcsv(filename)
    times = mylist[0]
    print('times0: %f' % times[0])
    print('times1: %f' % times[1])
    voltages = mylist[1]

    dt = times[1]-times[0]
    number_of_samples = int(math.floor(averaging_period/dt))

    number_of_windows = int(math.floor(len(times)/number_of_samples))

    hrlist = [hrlist_values] * number_of_windows

    myHRM = HRM(times, voltages, averaging_period = averaging_period)
    myHRM.avghr()
    print(len(myHRM.avghr_list))
    print(len(hrlist))
    assert myHRM.avghr_list == hrlist