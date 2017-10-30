def cardia_annotations(list, brady_bound, tachy_bound):

    """cardia_annotations

    Module Author: Hala El-Nahal

    Function: Outputs bradycardia and tachycardia annotation strings: strings of true or false

    Four input arguments:
        -arg 1: any list, instant or average HR
        -arg 2: bound for bradycardia
        -arg 3: bound for tachycardia

    Two outputs:
        -brady: bradycardia annotations
        -tachy: tachycardia annotations
    """

    # ----------------------------------------------------------------------------------------------------------------

    brady = []
    tachy = []
    for x in list:
        if x <= brady_bound:
            brady.append("true")
        if x > brady_bound:
            brady.append("false")
        if x >= tachy_bound:
            tachy.append("true")
        if x < tachy_bound:
            tachy.append("false")

    return [brady, tachy]



