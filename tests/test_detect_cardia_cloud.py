from Cardia_CloudECG import detect_cardia_cloud


def test_detect_cardia_cloud():
    [brady_inst_hr, tachy_inst_hr, brady_avg_hr, tachy_avg_hr ] = detect_cardia_cloud([60, 100, 50, 20, 200],
                                                                                      [60, 100, 50, 20, 200], 60, 100)
    assert brady_inst_hr == ['true', 'false', 'true', 'true', 'false']
    assert tachy_inst_hr == ['false', 'true', 'false', 'false', 'true']
    assert brady_avg_hr == ['true', 'false', 'true', 'true', 'false']
    assert tachy_avg_hr == ['false', 'true', 'false', 'false', 'true']

