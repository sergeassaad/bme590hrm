import sys
import os
import csv
import pytest
from ReadCSV import readCSV
from AvgHR import avgHR

def test_avgHR():

	HRlist = [48, 96, 144]

	list1 = readCSV('ECG_dummy_data_1_avgHR.csv')
	times1 = list1[0]
	voltages1 = list1[1]

	list2 = readCSV('ECG_dummy_data_2_avgHR.csv')
	times2 = list2[0]
	voltages2 = list2[1]

	list3 = readCSV('ECG_dummy_data_3_avgHR.csv')
	times3 = list3[0]
	voltages3 = list3[1]


	assert abs(avgHR(times1, voltages1)- HRlist[0])<5
	assert abs(avgHR(times2, voltages2)- HRlist[1])<5
	assert abs(avgHR(times3, voltages3)- HRlist[2])<5

	assert abs(avgHR(times1, voltages1,   times1[0]+0.5*(times1[len(times1)-1]-times1[0]),  times1[len(times1)-1])- HRlist[0])<5
	assert abs(avgHR(times2, voltages2,   times2[0]+0.5*(times1[len(times2)-1]-times2[0]),  times2[len(times2)-1])- HRlist[1])<5
	assert abs(avgHR(times3, voltages3,   times3[0]+0.5*(times3[len(times3)-1]-times3[0]),  times3[len(times3)-1])- HRlist[2])<5
	# assert abs(avgHR(times2, voltages2)- HRlist[1])<5
	# assert abs(avgHR(times3, voltages3)- HRlist[2])<5


	# assert avgHR(times2, voltages2) == HRlist[1]
	# assert avgHR(times3, voltages3) == HRlist[2]