from brady_tachy_annotations import cardia_annotations


def detect_cardia_cloud(inst_hr, avg_hr, brady_bound=60, tachy_bound=100):

    """detect_cardia_cloud

    Module Author: Hala El-Nahal

    Function: Outputs bradycardia and tachycardia annotation strings: strings of true or false

    Four input arguments:
        -arg 1: an instantaneous HR array
        -arg 2: an average HR array
        -arg 2: bound for bradycardia
        -arg 3: bound for tachycardia

    Two outputs:
        -brady: bradycardia annotations
        -tachy: tachycardia annotations
    """
    # ----------------------------------------------------------------------------------------------------------------
    [brady_inst_hr, tachy_inst_hr] = cardia_annotations(inst_hr, brady_bound,tachy_bound)
    [brady_avg_hr, tachy_avg_hr] = cardia_annotations(avg_hr, brady_bound, tachy_bound)

    return brady_inst_hr, tachy_inst_hr, brady_avg_hr, tachy_avg_hr






