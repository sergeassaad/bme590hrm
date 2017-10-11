from time_ranges import time_ranges


def detect_cardia(inst_hr, times, brady_bound, tachy_bound, display_time_ranges=True, diagnosis_time_threshold=1):

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

    i = 0
    if t_times != []:
        for x in t_times:
            if t_times[i][1]-t_times[i][0] >= diagnosis_time_threshold:
                diagnosis1 = 'Tachycardia detected'
                break
            else:
                diagnosis1 = 'No Tachycardia detected'
            i += 1
    else:
        diagnosis1 = 'No Tachycardia detected'

    i = 0
    if b_times != []:
        for x in b_times:
            if b_times[i][1]-b_times[i][0] >= diagnosis_time_threshold:
                diagnosis2 = 'Bradycardia detected'
                break
            else:
                diagnosis2 = 'No Bradycardia detected'
            i += 1
    else:
        diagnosis2 = 'No Bradycardia detected'

    diagnosis = "Diagnosis: {}, {}" .format(diagnosis1, diagnosis2)

    return [time_range, diagnosis]




