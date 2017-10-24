"""test_InstHR.py
Unit test for InstHR - a function that will calculate the instantaneous heart
rate.
"""
import os
import sys
import csv

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')


f = open('dummyEKGdata.csv', 'rU')
pointer = csv.reader(f)
exampleData = list(pointer)
f.close()
t = []
v = []
for i in range(1, len(exampleData)):
    t.append(float(exampleData[i][0]))
    v.append(float(exampleData[i][1]))


def test_inputs():
    from InstHR import ihr
    assert ihr('aaa', [1, 2, 3]) == ('Please input a list of times and'
                                     'a list of lead voltages as arguments.')
    assert ihr([1], [1, 2, 3]) == 'Please input lists with identical lengths.'


def test_hr_calc():
    from InstHR import ihr
    assert ihr(t, v)[0] == [(0.173, 0.517), (0.517, 0.923), (0.923, 1.267),
                            (1.267, 1.673), (1.673, 2.017),
                            (2.017, 2.423), (2.423, 2.767)]
    assert ihr(t, v)[1] == [174.0, 148.0, 174.0, 148.0, 174.0, 148.0, 174.0]


def test_class():
    from HeartRateMonitor import HRM
    obj = HRM(t, v)
    obj.ihr()
    assert obj.ihr_times == [(0.173, 0.517), (0.517, 0.923), (0.923, 1.267),
                             (1.267, 1.673), (1.673, 2.017),
                             (2.017, 2.423), (2.423, 2.767)]
    assert obj.instant_hr == [174.0, 148.0, 174.0, 148.0, 174.0, 148.0, 174.0]
