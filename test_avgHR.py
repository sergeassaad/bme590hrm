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


	assert avgHR(times1, voltages1) == HRlist[0]
	assert avgHR(times2, voltages2) == HRlist[1]
	assert avgHR(times3, voltages3) == HRlist[2]