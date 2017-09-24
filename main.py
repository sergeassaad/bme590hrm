"""main
Authors: Joseph Cobb, Hala El-Nahal, Serge Assad
Function:

"""

from READCSV import readCSV
from InstHR import ihr
from avgHR import
from

def main():

    combo()



def combo():

    data = readCSV(ecg_data.csv)
    times = data[0]
    voltages = data[1]
    data_2 = ihr(times, voltages)
    time_pairs = data_2[0]
    heart_rates = data_2[1]
    
    data_3 = detectcardia(time_pairs, heart_rates)


if __name__ == "__main__":
    main()
