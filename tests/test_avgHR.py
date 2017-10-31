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
    averaging_period = 10
    filename = 'ECG_dummy_data_1_avgHR.csv'
    mylist = readcsv(filename)
    times = mylist[0]
    voltages = mylist[1]
    expected = [54.857142857142854, 54.857142857142854, 54.857142857142854]
    myHRM = HRM(times, voltages, averaging_period = averaging_period)
    myHRM.avghr()
    print(len(myHRM.avghr_list))
    assert myHRM.avghr_list == expected


    averaging_period = 20
    filename = 'ECG_dummy_data_1_avgHR.csv'
    mylist = readcsv(filename)
    times = mylist[0]
    voltages = mylist[1]
    expected = [51.2, 54.857142857142854]
    myHRM = HRM(times, voltages, averaging_period = averaging_period)
    myHRM.avghr()
    print(len(myHRM.avghr_list))
    assert myHRM.avghr_list == expected

    averaging_period = 30
    filename = 'ECG_dummy_data_1_avgHR.csv'
    mylist = readcsv(filename)
    times = mylist[0]
    voltages = mylist[1]
    expected = [50.08695652173913]
    myHRM = HRM(times, voltages, averaging_period=averaging_period)
    myHRM.avghr()
    print(len(myHRM.avghr_list))
    assert myHRM.avghr_list == expected