class HRM:

    def __init__(self, times=[], voltages=[], time_units='s', t1=None, t2=None):
        self.times = times
        self.voltages = voltages
        self.time_units = time_units
        self.averagehr = -1
        if t1 is None:
            t1 = self.times[0]
        if t2 is None:
            t2 = self.times[len(self.times)-1]
        self.t1 = t1
        self.t2 = t2
        self.instant_hr = []
        self.ihr_times = []

    def avghr(self):
        from AvgHR import avghr
        self.averagehr = avghr(self.times, self.voltages, self.t1, self.t2)

    def ihr(self):
        from InstHR import ihr
        self.ihr_times, self.instant_hr = ihr(self.times, self.voltages)

    def detect_Cardia(self, inst_hr, times, display_time_ranges=True, diagnosis_time_threshold=1):
        from Cardia import detect_cardia
        return detect_cardia(inst_hr, times, display_time_ranges, diagnosis_time_threshold)
