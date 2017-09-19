def DetectCardia(instHR):
    diagnosis = []
    time = ([],[],[])
    for x in instHR:
        if x<60:
            diagnosis.append('Bradycardia')
        elif x>100:
            diagnosis.append('Tachycardia')
        elif x>=60 & x<=100:
            diagnosis.append('Normal')

    return diagnosis
