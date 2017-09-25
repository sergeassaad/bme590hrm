"""
ReadCSV.py
========
readcsv:

- Input: csv file
- Output: time vector, voltages vector
"""


import csv


def readcsv(filename):
    times = []
    voltages = []
    file = open(filename, "r")
    reader = csv.reader(file)
    row_count = 0

    for row in reader:
        if row_count > 0:
            times.append(float(row[0]))
            voltages.append(float(row[1]))
        row_count += 1

    return [times, voltages]
