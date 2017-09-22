
import sys
import os
import pytest


def avgHR(times, voltages):

	dt = times[1] - times[0] # assume constant sampling rate
	threshold_constant = 0.7
	threshold = threshold_constant*(max(voltages)-min(voltages)) + min(voltages)
	#print(threshold)
	peak_count = 0
	peak_times = []

	for i in range(0,len(voltages)-1):
		if (voltages[i]>=voltages[i-1] and voltages[i]>voltages[i+1]) and voltages[i]>threshold:
			peak_count += 1
			peak_times.append(times[i])

	return 60.0*peak_count/(peak_times[-1]-peak_times[0])




