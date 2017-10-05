"""test_ReadCSV.py
tests the readCSV for 2 dummy csv files"
"""
import os
import sys
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from ReadCSV import readcsv



def test_readcsv():
    assert readcsv('ECG_dummy_data_1.csv') == [[1, 2, 3], [0.1, 0.4, 0.6]]
    assert readcsv('ECG_dummy_data_2.csv') == [[0.1, 0.2, 0.3], [0.3, 0.3, 60]]
