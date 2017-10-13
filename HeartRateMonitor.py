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
        from AvgHR import avghr
        if t1 == -1 or t2 == -1:
            t1 = self.times[0]
            t2 = self.times[len(self.times)-1]
        return avghr(self.times, self.voltages, t1, t2)

    def ihr(self):
        from InstHR import ihr
        return ihr(self.times, self.voltages)

    def detect_Cardia(self, inst_hr, times, display_time_ranges=True, diagnosis_time_threshold=1):
        from Cardia import detect_cardia
        return detect_cardia(inst_hr, times, display_time_ranges, diagnosis_time_threshold)