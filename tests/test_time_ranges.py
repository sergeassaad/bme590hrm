import time_ranges


def test_time_ranges():

    x_times = time_ranges.time_ranges(["Tachycardia", "Normal", "Bradycardia"], [(0.0005, 0.00055), (0, 0.00005),
                                                                                 (0.0002, 0.00025)], "Normal")
    assert x_times == [(0, 0.00005)]

    x_times = time_ranges.time_ranges(["Tachycardia", "Normal", "Bradycardia"], [(0.0005, 0.00055), (0, 0.00005),
                                                                                 (0.0002, 0.00025)], "Tachycardia")
    assert x_times == [(0.0005, 0.00055)]

    x_times = time_ranges.time_ranges(["Tachycardia", "Normal", "Bradycardia"], [(0.0005, 0.00055), (0, 0.00005),
                                                                                 (0.0002, 0.00025)], "Bradycardia")
    assert x_times == [(0.0002, 0.00025)]

    x_times = time_ranges.time_ranges(["Tachycardia", "Tachycardia", "Normal", "Bradycardia"], [(0.0005, 0.00055),
                                                                                               (0.0006,0.00065),
                                                                                               (0, 0.00005),
                                                                                               (0.0002, 0.00025)],
                                      "Tachycardia")
    assert x_times == [(0.0005, 0.00065)]
