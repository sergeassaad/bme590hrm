class HRM:

    def __init__(self, times=[], voltages=[], time_units='s', t1=-1, t2=-1, display_time_ranges=True,
                 diagnosis_time_threshold=1):
        self.times = times
        self.voltages = voltages
        self.time_units = time_units
        self.averagehr = -1
        if t1 == -1:
            t1 = self.times[0]
        if t2 == -1:
            t2 = self.times[len(self.times)-1]
        self.t1 = t1
        self.t2 = t2
        self.display_time_ranges = display_time_ranges
        self.diagnosis_time_threshold = diagnosis_time_threshold

    def avghr(self):
        from AvgHR import avghr
        self.averagehr = avghr(self.times, self.voltages, self.t1, self.t2)

    def ihr(self):
        from InstHR import ihr
        return ihr(self.times, self.voltages)

    def detect_Cardia(self):
        from Cardia import detect_cardia
        self.DetectCardia = detect_cardia(inst_hr, times, self.display_time_ranges, self.diagnosis_time_threshold)