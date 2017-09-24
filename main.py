"""main
Authors: Joseph Cobb, Hala El-Nahal, Serge Assad
Function:

"""

from ReadCSV import readcsv
from InstHR import ihr
from AvgHR import avghr
from Cardia import detect_cardia

def main():
    time_bound1 = 0
    time_bound2 = 10
    time_ranges='timeRanges'
    diagnosis_time_threshold=0.001
    combo(time_bound1, time_bound2,time_ranges, diagnosis_time_threshold )



def combo(time_bound1, time_bound2, time_ranges, diagnosis_time_threshold):


    data = readcsv(ecg_data.csv)
    times = data[0]
    voltages = data[1]
    data_2 = ihr(times, voltages)
    time_pairs = data_2[0]
    heart_rates = data_2[1]
    avghr_value = avghr(times,voltages,time_bound1, time_bound2)
    data_3 = detect_cardia(time_pairs, heart_rates, time_ranges, diagnosis_time_threshold)
    timesranges = data_3[0]
    diagnosis = data_3[1]

if __name__ == "__main__":
    main()
