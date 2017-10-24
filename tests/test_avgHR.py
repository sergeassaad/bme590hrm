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
    averaging_period = 20
    hrlist_values = [48, 96, 144]

    filename = 'ECG_dummy_data_1_avgHR.csv'
    mylist = readcsv(filename)
    times = mylist[0]
    voltages = mylist[1]

    dt = times[1]-times[0]
    number_of_samples = int(math.floor(averaging_period/dt))

    hrlist = [hrlist_values[0]] * number_of_samples

    myHRM = HRM(times, voltages, averaging_period = averaging_period)
    assert myHRM.avghr() == hrlist