from math import isnan


def cardia_annotations(hr_list, brady_bound, tachy_bound):

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

    Throws error if brady_bound and tachy_bound are not integers
    """

    # ----------------------------------------------------------------------------------------------------------------
    try:
        brady = []
        tachy = []
        for x in hr_list:
            if x <= brady_bound:
                brady.append("true")
            if x > brady_bound:
                brady.append("false")
            if x >= tachy_bound:
                tachy.append("true")
            if x < tachy_bound:
                tachy.append("false")
            if isnan(x) is True:
                brady.append(float("NaN"))
                tachy.append(float("NaN"))

        return [brady, tachy]

    except Exception as e:
        print("brad_bound and tachy_bound must be integers")

