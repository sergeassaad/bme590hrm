def DetectCardia(instHR, times, timeRanges, diagnosisTimeThreshold):

    diagnosis = []
    for x in instHR:
        if x < 60:
            diagnosis.append("Bradycardia")
        elif x > 100:
            diagnosis.append("Tachycardia")
        elif x >= 60 & x <= 100:
            diagnosis.append("Normal")

    indexN = [i for i, x in enumerate(diagnosis) if x == "Normal"]
    indexT = [i for i, x in enumerate(diagnosis) if x == "Tachycardia"]
    indexB = [i for i, x in enumerate(diagnosis) if x == "Bradycardia"]

    nTimes1 = []
    tTimes1 = []
    bTimes1 = []

    for n in indexN:
        nTimes1.append(times[n])
    for n in indexT:
        tTimes1.append(times[n])
    for n in indexB:
        bTimes1.append(times[n])

    timestep = times[0][1]-times[0][0]

    i = 0
    if len(indexN) > 1:
        while i < len(nTimes1)-1:
            if nTimes1[i + 1][0] - nTimes1[i][1] <= timestep:
                nTimes1[i+1] = (nTimes1[i][0],nTimes1[i+1][1])
                del nTimes1[i]
            elif nTimes1[i + 1][0] - nTimes1[i][1] > timestep:
                i=i+1

    i = 0
    if len(indexT) > 1:
        while i < len(tTimes1) - 1:
            if tTimes1[i + 1][0] - tTimes1[i][1] <= timestep:
                tTimes1[i + 1] = (tTimes1[i][0], tTimes1[i + 1][1])
                del tTimes1[i]
            elif tTimes1[i + 1][0] - tTimes1[i][1] > timestep:
                i = i+1

    i = 0
    if len(indexB) > 1:
        while i < len(bTimes1) - 1:
            if bTimes1[i + 1][0] - bTimes1[i][1] <= timestep:
                bTimes1[i + 1] = (bTimes1[i][0], bTimes1[i + 1][1])
                del bTimes1[i]
            elif bTimes1[i + 1][0] - bTimes1[i][1] > timestep:
                i = i+1

    if timeRanges == 'timeRanges':
        timeRange = "Time ranges: Patient had a normal heart rate between {}, " \
                    "had tachycardia between {} and had bradycardia between {}".format(nTimes1, tTimes1, bTimes1)
    if timeRanges == 'noTimeRanges':
        timeRange = ''

    i = 0
    for x in tTimes1:
        if tTimes1[i][1]-tTimes1[i][0] >= diagnosisTimeThreshold:
            diagnosis1 = 'Tachycardia detected'
        else:
            diagnosis1 = 'No tachycardia detected'

    i = 0
    for x in bTimes1:
        if bTimes1[i][1]-bTimes1[i][0] >= diagnosisTimeThreshold:
            diagnosis2 = 'Bradycardia detected'
        else:
            diagnosis2 = 'No bradycardia detected'

    diagnosis = "Diagnosis: {}, {}" .format(diagnosis1, diagnosis2)

    return [timeRange, diagnosis]





