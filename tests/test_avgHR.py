import os
import sys
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from ReadCSV import readcsv
from AvgHR import avghr
from HeartRateMonitor import HRM



def test_avghr():

    hrlist = [48, 96, 144]

    list1 = readcsv('ECG_dummy_data_1_avgHR.csv')
    times1 = list1[0]
    voltages1 = list1[1]

    list2 = readcsv('ECG_dummy_data_2_avgHR.csv')
    times2 = list2[0]
    voltages2 = list2[1]

    list3 = readcsv('ECG_dummy_data_3_avgHR.csv')
    times3 = list3[0]
    voltages3 = list3[1]

    HRM1 = HRM(times1,voltages1)
    HRM2 = HRM(times2, voltages2)
    HRM3 = HRM(times3, voltages3)

    HRM1.avghr()
    HRM2.avghr()
    HRM3.avghr()


    assert abs(avghr(times1, voltages1) - hrlist[0])<5
    assert abs(avghr(times2, voltages2) - hrlist[1])<5
    assert abs(avghr(times3, voltages3) - hrlist[2])<5

    lower_bound1 = times1[0]+0.5*(times1[len(times1)-1]-times1[0])
    lower_bound2 = times2[0]+0.5*(times2[len(times2)-1]-times2[0])
    lower_bound3 = times3[0]+0.5*(times3[len(times3)-1]-times3[0])
    assert abs(avghr(times1, voltages1,   lower_bound1,  times1[len(times1)-1]) - hrlist[0]) < 5
    assert abs(avghr(times2, voltages2,   lower_bound2,  times2[len(times2)-1]) - hrlist[1]) < 5
    assert abs(avghr(times3, voltages3,   lower_bound3,  times3[len(times3)-1]) - hrlist[2]) < 5

    assert abs(HRM1.averagehr - hrlist[0]) < 5
    assert abs(HRM2.averagehr - hrlist[1]) < 5
    assert abs(HRM3.averagehr - hrlist[2]) < 5

    lower_bound1 = times1[0] + 0.5 * (times1[len(times1) - 1] - times1[0])
    lower_bound2 = times2[0] + 0.5 * (times2[len(times2) - 1] - times2[0])
    lower_bound3 = times3[0] + 0.5 * (times3[len(times3) - 1] - times3[0])

    HRM1.t1 = lower_bound1
    HRM2.t1 = lower_bound2
    HRM3.t1 = lower_bound3

    HRM1.t2 = times1[len(times1)-1]
    HRM2.t2 = times2[len(times2)-1]
    HRM3.t2 = times3[len(times3)-1]

    HRM1.avghr()
    HRM2.avghr()
    HRM3.avghr()

    assert abs(HRM1.averagehr - hrlist[0]) < 5
    assert abs(HRM2.averagehr - hrlist[1]) < 5
    assert abs(HRM3.averagehr - hrlist[2]) < 5


