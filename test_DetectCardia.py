import Cardia

def test_DetectCardia():
    [diagnosis, times] = Cardia.DetectCardia([90,50,110], ([0,0.00005],[0.0002,0.00025],[0.0006,0.00065]))
    assert [diagnosis,times] == [['Normal', 'Bradycardia','Tachycardia'],([0,0.00005],[0.0002,0.00025],[0.0006,0.00065])]


