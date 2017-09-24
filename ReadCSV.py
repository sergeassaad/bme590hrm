"""ReadCSV.py
readCSV(filename) takes in a CSV file and outputs a list of 2 lists: 1st list = time, 2nd list = voltages
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
