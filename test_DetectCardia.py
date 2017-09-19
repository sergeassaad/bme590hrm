import Cardia

def test_DetectCardia():
    diagnosis = Cardia.DetectCardia([90,50,110])
    assert diagnosis == ['Normal', 'Bradycardia','Tachycardia']



