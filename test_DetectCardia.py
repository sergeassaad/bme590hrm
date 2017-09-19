

def test_DetectCardia():
    (diagnosis,time) = DetectCardia([90,50,110],([0,0.00005],[0.00085,0.0009],[0.0011,0.00115]))
    assert diagnosis == ['Normal', 'Bradycardia','tachycardia']
    assert time == ([90,50,110],([0,0.00005],[0.00085,0.0009],[0.0011,0.00115]))
