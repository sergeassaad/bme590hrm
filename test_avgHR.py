

from ReadCSV import readCSV
from AvgHR import avghr


def test_avghr():

    hrlist = [48, 96, 144]

    list1 = readCSV('ECG_dummy_data_1_avgHR.csv')
    times1 = list1[0]
    voltages1 = list1[1]

    list2 = readCSV('ECG_dummy_data_2_avgHR.csv')
    times2 = list2[0]
    voltages2 = list2[1]

    list3 = readCSV('ECG_dummy_data_3_avgHR.csv')
    times3 = list3[0]
    voltages3 = list3[1]

    assert abs(avghr(times1, voltages1) - hrlist[0])<5
    assert abs(avghr(times2, voltages2) - hrlist[1])<5
    assert abs(avghr(times3, voltages3) - hrlist[2])<5

    lower_bound1 = times1[0]+0.5*(times1[len(times1)-1]-times1[0])
    lower_bound2 = times2[0]+0.5*(times2[len(times2)-1]-times2[0])
    lower_bound3 = times3[0]+0.5*(times3[len(times3)-1]-times3[0])
    assert abs(avghr(times1, voltages1,   lower_bound1,  times1[len(times1)-1]) - hrlist[0]) < 5
    assert abs(avghr(times2, voltages2,   lower_bound2,  times2[len(times2)-1]) - hrlist[1]) < 5
    assert abs(avghr(times3, voltages3,   lower_bound3,  times3[len(times3)-1]) - hrlist[2]) < 5
