import diagnosis


def test_diagnosis():
    final_diagnosis = diagnosis.diagnosis([(0.0002, 0.00035)], [(0.0005, 0.00065), (0.0018, 0.00185)], 0.1)

    assert final_diagnosis == "Diagnosis: No Tachycardia detected, No Bradycardia detected"
