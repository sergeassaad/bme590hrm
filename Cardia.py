def detect_cardia(inst_hr, times, display_time_ranges=True, diagnosis_time_threshold=1):

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

    diagnosis = []
    for x in inst_hr:
        if x < 60:
            diagnosis.append("Bradycardia")
        elif x > 100:
            diagnosis.append("Tachycardia")
        elif x >= 60 & x <= 100:
            diagnosis.append("Normal")

    index_n = [i for i, x in enumerate(diagnosis) if x == "Normal"]
    index_t = [i for i, x in enumerate(diagnosis) if x == "Tachycardia"]
    index_b = [i for i, x in enumerate(diagnosis) if x == "Bradycardia"]

    n_times = []
    t_times = []
    b_times = []

    for n in index_n:
        n_times.append(times[n])
    for n in index_t:
        t_times.append(times[n])
    for n in index_b:
        b_times.append(times[n])

    timestep = times[0][1]-times[0][0]

    i = 0
    if len(index_n) > 1:
        while i < len(n_times)-1:
            if n_times[i + 1][0] - n_times[i][1] <= timestep:
                n_times[i+1] = (n_times[i][0],n_times[i+1][1])
                del n_times[i]
            elif n_times[i + 1][0] - n_times[i][1] > timestep:
                i = i+1

    i = 0
    if len(index_t) > 1:
        while i < len(t_times) - 1:
            if t_times[i + 1][0] - t_times[i][1] <= timestep:
                t_times[i + 1] = (t_times[i][0], t_times[i + 1][1])
                del t_times[i]
            elif t_times[i + 1][0] - t_times[i][1] > timestep:
                i = i+1

    i = 0
    if len(index_b) > 1:
        while i < len(b_times) - 1:
            if b_times[i + 1][0] - b_times[i][1] <= timestep:
                b_times[i + 1] = (b_times[i][0], b_times[i + 1][1])
                del b_times[i]
            elif b_times[i + 1][0] - b_times[i][1] > timestep:
                i = i+1

    if display_time_ranges:
        time_range = "Time ranges: Patient had a normal heart rate between {}, " \
                    "had tachycardia between {} and had bradycardia between {}".format(n_times, t_times, b_times)
    else:
        time_range = ''

    i = 0
    for x in t_times:
        if t_times[i][1]-t_times[i][0] >= diagnosis_time_threshold:
            diagnosis1 = 'Tachycardia detected'
        else:
            diagnosis1 = 'No Tachycardia detected'

    i = 0
    for x in b_times:
        if b_times[i][1]-b_times[i][0] >= diagnosis_time_threshold:
            diagnosis2 = 'Bradycardia detected'
        else:
            diagnosis2 = 'No Bradycardia detected'

    diagnosis = "Diagnosis: {}, {}" .format(diagnosis1, diagnosis2)

    return [time_range, diagnosis]




