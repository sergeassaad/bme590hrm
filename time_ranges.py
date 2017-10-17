def time_ranges(diagnoses, times, condition):
    index_x = [i for i, x in enumerate(diagnoses) if x == condition]

    x_times = []

    for n in index_x:
        x_times.append(times[n])

    timestep = times[0][1] - times[0][0]

    i = 0
    if len(index_x) > 1:
        while i < len(x_times) - 1:
            if x_times[i + 1][0] - x_times[i][1] <= timestep:
                x_times[i + 1] = (x_times[i][0], x_times[i + 1][1])
                del x_times[i]
            elif x_times[i + 1][0] - x_times[i][1] > timestep:
                i = i + 1

    return x_times