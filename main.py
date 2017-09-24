"""main
Authors: Joseph Cobb, Hala El-Nahal, Serge Assad
Function: Read input ECG data and output heart rate and tachycardia/ bradycardia detection
"""

from ReadCSV import readcsv
from InstHR import ihr
from AvgHR import avghr
from Cardia import detect_cardia


def main():

    time_bound1 = 0
    time_bound2 = float('INF')
    display_time_ranges = True
    diagnosis_time_threshold = 1
    combo(time_bound1, time_bound2, display_time_ranges, diagnosis_time_threshold)


def combo(time_bound1, time_bound2, display_time_ranges, diagnosis_time_threshold):

    data = readcsv(ecg_data.csv)
    times = data[0]
    voltages = data[1]

    data_2 = ihr(times, voltages)
    time_pairs = data_2[0]
    heart_rates = data_2[1]

    avg_hr_value = avghr(times, voltages, time_bound1, time_bound2)

    data_3 = detect_cardia(time_pairs, heart_rates, display_time_ranges, diagnosis_time_threshold)
    time_ranges = data_3[0]
    diagnosis = data_3[1]

    f = open('output.txt', 'w')
    f.write('%s \n' % diagnosis)

    if display_time_ranges:
        f.write('%s' % time_ranges)

    f.write('The average heart rate was %d between %d and %d.\n' % (avg_hr_value, time_bound1, time_bound2))

    f.write('The instantaneous heart rate was calculated for each heartbeat.\n')

    for i in range(len(heart_rates)):
        f.write('The heart rate was %d between %d and %d.\n' %(heart_rates[i], time_pairs[i][0], time_pairs[i][1]))

    f.close()


if __name__ == "__main__":
    main()
