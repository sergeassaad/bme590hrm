class HeartRateMonitor:
    avghr = -1
    insthr = []
    times_insthr = []
    diagnosis = ''
    times_diagnosis = []

    def __init__(self, times=[], voltages=[], time_units='s'):
        self.times = times
        self.voltages = voltages
