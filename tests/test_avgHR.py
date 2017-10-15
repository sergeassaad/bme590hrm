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
        # assert abs(avghr(times, voltages) - hrlist[i]) < 5

        myHRM = HRM(times,voltages)
        # myHRM.avghr()
        # assert(abs(myHRM.averagehr - hrlist[i-1]) < 5)
        assert (abs(myHRM.avghr() - hrlist[i - 1]) < 5)
        lower_bound = times[0] + 0.5 * (times[len(times) - 1] - times[0])
        assert abs(avghr(times, voltages, lower_bound, times[len(times) - 1]) - hrlist[i-1]) < 5