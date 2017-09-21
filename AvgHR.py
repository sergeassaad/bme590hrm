
import sys
import os
import pytest


def avgHR(times, voltages):

	dt = times[1] - times[0] # assume constant sampling rate
	threshold_constant = 0.9
	threshold = threshold_constant*(max(voltages)-min(voltages)) + min(voltages)
	#print(threshold)

	index = [i for i, x in enumerate(voltages) if x > threshold]
	#print(index)
	voltages_thresh = [voltages[i] for i in index]
	times_thresh = [times[i] for i in index]
	#print(len(times_thresh))

	peak_count = 1
	peak_times = []
	for i in range(1,len(index)):
		if(times_thresh[i]-times_thresh[i-1] > dt):
			peak_times.append(times_thresh[i-1])
			#print(times_thresh[i-1])
			peak_count += 1

	print peak_count
	return 60*peak_count/(peak_times[-1]-peak_times[0])




