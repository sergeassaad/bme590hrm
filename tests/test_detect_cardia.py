import os
import sys
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
import Cardia


def test_detect_cardia():
    [time_range, diagnosis] = Cardia.detect_cardia([110, 90, 50, 110, 70, 70, 70, 40, 40, 110],
                                                   [(0.0005, 0.00055), (0, 0.00005), (0.0002, 0.00025),
                                                    (0.0006, 0.00065), (0.00005, 0.0001), (0.0001, 0.00015),
                                                    (0.00015, 0.0002),
                                                    (0.00025, 0.0003), (0.0003, 0.00035), (0.0018, 0.00185)],
                                                   False, 0.0001)
    assert [time_range, diagnosis] == ['', "Diagnosis: Tachycardia detected, Bradycardia detected"]

    [time_range, diagnosis] = Cardia.detect_cardia([110, 90, 50, 110, 70, 70, 70, 40, 40, 110],
                                                   [(0.0005, 0.00055), (0, 0.00005), (0.0002, 0.00025),
                                                    (0.0006, 0.00065), (0.00005, 0.0001), (0.0001, 0.00015),
                                                    (0.00015, 0.0002),
                                                    (0.00025, 0.0003), (0.0003, 0.00035), (0.0018, 0.00185)],
                                                   True, 0.0001)
    assert [time_range, diagnosis] == ["Time ranges: Patient had a normal heart rate between [(0, 0.0002)], "
                                       "had tachycardia between [(0.0005, 0.00065), (0.0018, 0.00185)] and had "
                                       "bradycardia between [(0.0002, 0.00035)]",
                                       "Diagnosis: Tachycardia detected, Bradycardia detected"]

    [time_range, diagnosis] = Cardia.detect_cardia([110, 90, 50, 110, 70, 70, 70, 40, 40, 110],
                                                   [(0.0005, 0.00055), (0, 0.00005), (0.0002, 0.00025),
                                                    (0.0006, 0.00065), (0.00005, 0.0001), (0.0001, 0.00015),
                                                    (0.00015, 0.0002),
                                                    (0.00025, 0.0003), (0.0003, 0.00035), (0.0018, 0.00185)],
                                                   True, 0.1)
    assert [time_range, diagnosis] == ["Time ranges: Patient had a normal heart rate between [(0, 0.0002)], "
                                       "had tachycardia between [(0.0005, 0.00065), (0.0018, 0.00185)] and had "
                                       "bradycardia between [(0.0002, 0.00035)]",
                                       "Diagnosis: No Tachycardia detected, No Bradycardia detected"]
