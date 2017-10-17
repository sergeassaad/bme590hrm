def diagnosis(b_times, t_times, diagnosis_time_threshold):
    diag1a = 'Tachycardia detected'
    diag1b = 'No Tachycardia detected'
    diag2a = 'Bradycardia detected'
    diag2b = 'No Bradycardia detected'

    i = 0
    if len(t_times) >= 1:
        for x in t_times:
            if t_times[i][1] - t_times[i][0] >= diagnosis_time_threshold:
                diagnosis1 = diag1a
                break
            else:
                diagnosis1 = diag1b
            i += 1
    else:
        diagnosis1 = diag1b

    i = 0
    if len(b_times) >= 1:
        for x in b_times:
            if b_times[i][1] - b_times[i][0] >= diagnosis_time_threshold:
                diagnosis2 = diag2a
                break
            else:
                diagnosis2 = diag2b
            i += 1
    else:
        diagnosis2 = diag2b

    final_diagnosis = "Diagnosis: {}, {}".format(diagnosis1, diagnosis2)

    return final_diagnosis
