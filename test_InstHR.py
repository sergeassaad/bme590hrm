"""test_InstHR.py
Unit test for InstHR - a function that will calculate the instantaneous heart rate.
"""

import csv
from InstHR import ihr

f = open('dummyEKGdata.csv', 'rU')
pointer = csv.reader(f)
exampledata = list(pointer)
t = []
v = []
for i in range(1,len(exampledata)):
    t.append(exampledata[i][0])
    v.append(exampledata[i][1])


def test_inputs():

    assert ihr('aaa', [1, 2, 3]) == 'Please input a list of times and a list of lead voltages as arguments.'
    assert ihr([1], [1, 2, 3]) == 'Please input a lists with identical lengths.'


def hr_calc():

    assert ihr(t,v) == 0

