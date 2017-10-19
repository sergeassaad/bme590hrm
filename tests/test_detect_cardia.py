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

obj = HRM(t, v)
obj.ihr()
obj.detect_cardia()

def test_detect_cardia_class():
    assert obj.DetectCardia == ['Time ranges: Patient had a normal heart rate between [], had tachycardia '
                                'between [(0.173, 2.767)], and had bradycardia between []', 'Diagnosis: '
                                                                                            'Tachycardia detected, '
                                                                                            'No Bradycardia detected']


