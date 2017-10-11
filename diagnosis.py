def diagnosis(b_times, t_times, diagnosis_time_threshold):
    i = 0
    if len(t_times) >= 1:
        for x in t_times:
            if t_times[i][1] - t_times[i][0] >= diagnosis_time_threshold:
                diagnosis1 = 'Tachycardia detected'
                break
            else:
                diagnosis1 = 'No Tachycardia detected'
            i += 1
    else:
        diagnosis1 = 'No Tachycardia detected'

    i = 0
    if len(b_times) >= 1:
        for x in b_times:
            if b_times[i][1] - b_times[i][0] >= diagnosis_time_threshold:
                diagnosis2 = 'Bradycardia detected'
                break
            else:
                diagnosis2 = 'No Bradycardia detected'
            i += 1
    else:
        diagnosis2 = 'No Bradycardia detected'

    final_diagnosis = "Diagnosis: {}, {}".format(diagnosis1, diagnosis2)

    return final_diagnosis
