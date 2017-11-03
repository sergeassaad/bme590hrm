class HRM:
    """
    HeartRateMonitor.py
    ========
    Methods:

    -	avghr (calculates average HR)
    -	ihr (calculates instantaneous HR)
    -   detect_cardia (finds brady- and tachycardia occurrences)
    """
    def __init__(self, times=[], voltages=[], time_units='s', t1=None, t2=None,
                averaging_period=1, brady_bound=60, tachy_bound=100):
        self.times = times
        self.voltages = voltages
        self.time_units = time_units
        self.brady_bound = brady_bound
        self.tachy_bound = tachy_bound
        self.average_hr = None
        self.avghr_list = None
        if t1 is None:
            t1 = self.times[0]
        if t2 is None:
            t2 = self.times[len(self.times)-1]
        self.t1 = t1
        self.t2 = t2
        self.averaging_period = averaging_period
        self.instant_hr = []
        self.ihr_times = []
        self.tachy_avg = []
        self.brady_avg=[]
        self.tachy_inst = []
        self.brady_inst = []

    def avghr(self):
        """
        AvgHR.py
        ========
        avghr:

        -	Input: Lists of times, list of voltages, lower time bound, upper time bound
        -	Output: 1 value for average heart rate for the specified time range
        """
        from AvgHR import avghr
        from AvgHR import avghr_period
        self.average_hr = avghr(self.times, self.voltages, self.t1, self.t2)
        self.avghr_list = avghr_period(self.times, self.voltages, self.averaging_period)
        return self.average_hr

    def ihr(self):
        peak_times = []
        voltages = []
        heart_rates = []
        max_v = float(max(self.voltages))
        min_v = float(min(self.voltages))
        threshold_constant = float(0.75)
        threshold = threshold_constant * (max_v - min_v) + min_v

        for i in range(len(self.voltages) - 1):
            if (self.voltages[i] >= threshold and
                    self.voltages[i] >= self.voltages[i - 1] and
                    self.voltages[i] > self.voltages[i + 1]):
                if round(self.times[i], 3) not in peak_times:
                    peak_times.append(round(self.times[i], 3))
                    voltages.append(self.voltages[i])

        time_pairs = []

        for i in range(len(peak_times) - 1):
            time_pairs.append((peak_times[i], peak_times[i + 1]))

        for i in range(len(time_pairs)):
            heart_rates.append(round(60 /
                                     float(
                                         time_pairs[i][1] - time_pairs[i][0])))

        instant_hr = [float('nan') for _ in range(len(self.times))]

        for i in range(len(self.times)):
            for j in range(len(time_pairs)):
                if self.times[i] >= time_pairs[j][0] and \
                                self.times[i] <= time_pairs[j][1]:
                    instant_hr[i] = heart_rates[j]

        self.ihr_times = self.times
        self.instant_hr = instant_hr
        return self.instant_hr

    def detect_cardia(self):
        """
        Cardia_CloudECG.py
        ========
        detect_cardia_cloud:

        -	Input: List of instantaneous heart rates, list of average heart rates, bradycardia threshold,
            tachycardia threshold
        -	Output: bradycardia and tachycardia annotations for instantaneous and average heart rate lists
        """
        from Cardia_CloudECG import detect_cardia_cloud
        [self.brady_inst, self.tachy_inst, self.brady_avg, self.tachy_avg] = \
            detect_cardia_cloud(self.instant_hr, self.avghr_list, self.brady_bound,
                                          self.tachy_bound)

