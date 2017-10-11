from time_ranges import time_ranges
from diagnosis import diagnosis


def detect_cardia(inst_hr, times, brady_bound=60, tachy_bound=100, display_time_ranges=True, diagnosis_time_threshold=1):

    """detect_cardia

    Module Author: Hala El-Nahal

    Function: Outputs a string listing the time ranges during which the patient's instantaneous heart rate was normal,
    the time ranges during which there was bradycardia (instantaneous HR below 60bpm) and the time ranges during which
    there was tachycardia (instantaneous HR above 100bpm). Also outputs an overall diagnosis of tachycardia or
    bradycardia based on a threshold set by the user

    Four input arguments:
        -arg 1: an instantaneous HR array
        -arg 2: an array of time ranges that correspond to the instantaneous HRs in arg1
        -arg 3: (user input) A boolean that displays time ranges described above when set to true and does not display
                the time ranges when set to false. Default set to true.
        -arg 4: (user input) the amount of time in seconds that the instantaneous HR must remain under 60bpm or over
                100bpm for program to indicate that bradycardia or tachycardia, respectively, (or both) was detected.
                In other words, a time threshold for bradycardia and tachycardia detection. Default set to 1 second.

    Two outputs:
        -Time ranges for normal, bradycardia and tachycardia instantaneous HRs
        -Overall diagnosis (for example: 'tachycardia detected') based on the threshold set by the user"""
    # ----------------------------------------------------------------------------------------------------------------

    # time ranges for normal, tachycardia and bradycardia instant HR
    diag = []
    for x in inst_hr:
        if x < brady_bound:
            diag.append("Bradycardia")
        elif x > tachy_bound:
            diag.append("Tachycardia")
        elif x >= brady_bound & x <= tachy_bound:
            diag.append("Normal")

    n_times = time_ranges(diag, times, "Normal")
    b_times = time_ranges(diag, times, "Bradycardia")
    t_times = time_ranges(diag, times, "Tachycardia")

    if display_time_ranges:
        time_range = "Time ranges: Patient had a normal heart rate between {}, " \
                    "had tachycardia between {}, and had bradycardia between {}".format(n_times, t_times, b_times)
    else:
        time_range = ''

    # overall diagnosis based on diagnosis threshold set by user
    final_diagnosis = diagnosis(b_times, t_times, diagnosis_time_threshold)

    return [time_range, final_diagnosis]




