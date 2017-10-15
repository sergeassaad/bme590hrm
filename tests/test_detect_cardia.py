import os
import sys
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from Cardia import detect_cardia
from HeartRateMonitor import HRM

inst_hr = [110, 90, 50, 110, 70, 70, 70, 40, 40, 110]
time_pairs = [(0.0005, 0.00055), (0, 0.00005), (0.0002, 0.00025),
                                                    (0.0006, 0.00065), (0.00005, 0.0001), (0.0001, 0.00015),
                                                    (0.00015, 0.0002),
                                                    (0.00025, 0.0003), (0.0003, 0.00035), (0.0018, 0.00185)]
display_time_ranges = False
diagnosis_time_threshold = 0.0001

HRM1 = HRM(inst_hr, time_pairs, display_time_ranges, diagnosis_time_threshold)


def test_detect_cardia():
    assert detect_cardia([110, 90, 50, 110, 70, 70, 70, 40, 40, 110],
                                                   [(0.0005, 0.00055), (0, 0.00005), (0.0002, 0.00025),
                                                    (0.0006, 0.00065), (0.00005, 0.0001), (0.0001, 0.00015),
                                                    (0.00015, 0.0002),
                                                    (0.00025, 0.0003), (0.0003, 0.00035), (0.0018, 0.00185)],
                                                   False, 0.0001) == \
           ['', 'Diagnosis: Tachycardia detected, Bradycardia detected']

    assert detect_cardia([110, 90, 50, 110, 70, 70, 70, 40, 40, 110],
                                                   [(0.0005, 0.00055), (0, 0.00005), (0.0002, 0.00025),
                                                    (0.0006, 0.00065), (0.00005, 0.0001), (0.0001, 0.00015),
                                                    (0.00015, 0.0002),
                                                    (0.00025, 0.0003), (0.0003, 0.00035), (0.0018, 0.00185)],
                                                   True, 0.0001) == \
           ["Time ranges: Patient had a normal heart rate between [(0, 0.0002)], "
                                       "had tachycardia between [(0.0005, 0.00065), (0.0018, 0.00185)], and had "
                                       "bradycardia between [(0.0002, 0.00035)]",
                                       "Diagnosis: Tachycardia detected, Bradycardia detected"]

    assert detect_cardia([110, 90, 50, 110, 70, 70, 70, 40, 40, 110],
                                                   [(0.0005, 0.00055), (0, 0.00005), (0.0002, 0.00025),
                                                    (0.0006, 0.00065), (0.00005, 0.0001), (0.0001, 0.00015),
                                                    (0.00015, 0.0002),
                                                    (0.00025, 0.0003), (0.0003, 0.00035), (0.0018, 0.00185)],
                                                   True, 0.1) == \
           ["Time ranges: Patient had a normal heart rate between [(0, 0.0002)], "
                                       "had tachycardia between [(0.0005, 0.00065), (0.0018, 0.00185)], and had "
                                       "bradycardia between [(0.0002, 0.00035)]",
                                       "Diagnosis: No Tachycardia detected, No Bradycardia detected"]


def test_detect_cardia_class():
    HRM1.detect_cardia()
    assert HRM1.DetectCardia == ['', 'Diagnosis: Tachycardia detected, Bradycardia detected']


