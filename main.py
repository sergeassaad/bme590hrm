"""main
Authors: Joseph Cobb, Hala El-Nahal, Serge Assad
Function: Read input ECG data and output heart rate and tachycardia/
bradycardia detection
"""

from AvgHR import avghr
from Cardia import detect_cardia
from ReadCSV import readcsv
from InstHR import ihr


def main():
  
    kwargs = {'time_bound1': 0, 'time_bound2': float('INF'),
              'display_time_ranges': True, 'diagnosis_time_threshold': 1, 'brady_bound': 60, 'tachy_bound':100}
    combo(**kwargs)

def combo(time_bound1, time_bound2, display_time_ranges,
          diagnosis_time_threshold, brady_bound, tachy_bound, input_filename='test_data/test_data1.csv',
          output_filename='output.txt'):

    data = readcsv(input_filename)

    times = data[0]
    voltages = data[1]

    data_2 = ihr(times, voltages)
    time_pairs = data_2[0]
    heart_rates = data_2[1]

    avg_hr_value = avghr(times, voltages, time_bound1, time_bound2)

    data_3 = detect_cardia(heart_rates, time_pairs, brady_bound, tachy_bound, display_time_ranges,
                           diagnosis_time_threshold)
    time_ranges = data_3[0]
    diagnosis = data_3[1]

    with open(output_filename, 'w') as f:
        f.write('%s \n' % diagnosis)

        if display_time_ranges:
            f.write('%s' % time_ranges)

        f.write('The average heart rate was %f between %f and %f.\n'
                % (avg_hr_value, time_bound1, time_bound2))
        f.write('The instantaneous heart rate was calculated'
                'for each heartbeat.\n')

        for i in range(len(heart_rates)):
            f.write('The heart rate was %d bpm between %f and %f seconds.\n'
                    % (heart_rates[i], time_pairs[i][0], time_pairs[i][1]))


if __name__ == "__main__":
    main()
