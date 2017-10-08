class HRM:
    avghr = -1
    insthr = []
    times_insthr = []
    diagnosis = ''
    times_diagnosis = []

    def __init__(self, times=[], voltages=[], time_units='s'):
        self.times = times
        self.voltages = voltages

    def avghr(self, t1=-1, t2=-1):
        from AvgHR import *
        if t1 == -1 or t2== -1:
            t1 = self.times[0]
            t2 = self.times[len(self.times)-1]
        return avghr(self.times, self.voltages, t1, t2)