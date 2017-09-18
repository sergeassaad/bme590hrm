"""ReadCSV.py
"""

import sys
import os
import csv

def readCSV(filename):
	times = []
	voltages = []
	file = open(filename, "rb")
	reader = csv.reader(file)
	row_count = 0;

	for row in reader:
		if row_count > 0:
			times.append(float(row[0]))
			voltages.append(float(row[1]))
		row_count += 1

	return [times, voltages]
