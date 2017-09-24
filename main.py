"""main
Authors: Joseph Cobb, Hala El-Nahal, Serge Assad
Function:

"""

from ReadCSV import readcsv
from InstHR import ihr
from AvgHR import avghr

def main():
    time_bound1 = 0
    time_bound2 = 10
    combo(time_bound1, time_bound2)



def combo(time_bound1, time_bound2):


    data = readcsv(ecg_data.csv)
    times = data[0]
    voltages = data[1]
    data_2 = ihr(times, voltages)
    time_pairs = data_2[0]
    heart_rates = data_2[1]
    avghr_value = avghr(times,voltages,time_bound1, time_bound2)
    data_3 = detectcardia(time_pairs, heart_rates)


if __name__ == "__main__":
    main()
