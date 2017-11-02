import os
import sys
import csv

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from Cardia import detect_cardia
from HeartRateMonitor import HRM

f = open('dummyEKGdata.csv', 'rU')
pointer = csv.reader(f)
exampleData = list(pointer)
f.close()
t = []
v = []
for i in range(1, len(exampleData)):
    t.append(float(exampleData[i][0]))
    v.append(float(exampleData[i][1]))
averaging_period = 20

obj = HRM(t, v, averaging_period = averaging_period)
obj.ihr()
obj.avghr()
obj.detect_cardia()

def test_detect_cardia_class():
    assert obj.tachy_avg == ['true']
    assert obj.brady_avg == ['false']
    assert obj.tachy_inst == ['true', 'true', 'true', 'true', 'true', 'true', 'true']
    assert obj.brady_inst == ['false', 'false', 'false', 'false', 'false', 'false', 'false']


