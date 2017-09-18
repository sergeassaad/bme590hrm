"""test_ReadCSV.py
"""

import sys
import os
import csv
import pytest
from ReadCSV import readCSV

def test_ReadCSV():
	assert readCSV('ECG_dummy_data_1.csv') == [[1,2,3], [0.1, 0.4, 0.6]]
	assert readCSV('ECG_dummy_data_2.csv') == [[0.1,0.2,0.3], [0.3, 0.3, 60]]