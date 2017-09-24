import Cardia

def test_DetectCardia():
    [timeRange, diagnosis] = Cardia.DetectCardia([110, 90, 50, 110, 70, 70, 70, 40, 40, 110],
                                                 [(0.0005, 0.00055), (0, 0.00005), (0.0002, 0.00025),
                                                  (0.0006, 0.00065), (0.00005, 0.0001), (0.0001, 0.00015),
                                                  (0.00015, 0.0002),
                                                  (0.00025, 0.0003), (0.0003, 0.00035), (0.0018, 0.00185)],
                                                 'noTimeRanges', 0.0001)
    assert [timeRange, diagnosis] == ['', "Diagnosis: Tachycardia detected, Bradycardia detected"]

    [timeRange, diagnosis] = Cardia.DetectCardia([110, 90, 50, 110, 70, 70, 70, 40, 40, 110],
                                                 [(0.0005, 0.00055), (0, 0.00005), (0.0002, 0.00025),
                                                  (0.0006, 0.00065), (0.00005, 0.0001), (0.0001, 0.00015),
                                                  (0.00015, 0.0002),
                                                  (0.00025, 0.0003), (0.0003, 0.00035), (0.0018, 0.00185)],
                                                 'timeRanges', 0.0001)
    assert [timeRange, diagnosis] == ["Time ranges: Patient had a normal heart rate between [(0, 0.0002)], "
                                      "had tachycardia between [(0.0005, 0.00065), (0.0018, 0.00185)] and had "
                                      "bradycardia between [(0.0002, 0.00035)]",
                                      "Diagnosis: Tachycardia detected, Bradycardia detected"]

    [timeRange, diagnosis] = Cardia.DetectCardia([110, 90, 50, 110, 70, 70, 70, 40, 40, 110],
                                                 [(0.0005, 0.00055), (0, 0.00005), (0.0002, 0.00025),
                                                  (0.0006, 0.00065), (0.00005, 0.0001), (0.0001, 0.00015),
                                                  (0.00015, 0.0002),
                                                  (0.00025, 0.0003), (0.0003, 0.00035), (0.0018, 0.00185)],
                                                 'timeRanges', 0.1)
    assert [timeRange, diagnosis] == ["Time ranges: Patient had a normal heart rate between [(0, 0.0002)], "
                                      "had tachycardia between [(0.0005, 0.00065), (0.0018, 0.00185)] and had "
                                      "bradycardia between [(0.0002, 0.00035)]",
                                      "Diagnosis: No tachycardia detected, No bradycardia detected"]
