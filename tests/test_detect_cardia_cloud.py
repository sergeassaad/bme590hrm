from Cardia_CloudECG import detect_cardia_cloud


def test_detect_cardia_cloud():
    assert detect_cardia_cloud([60, 100], [60, 100], 60, 100) == [["true", "false"], ["false", "true"]], [["true", "false"], ["false", "true"]]