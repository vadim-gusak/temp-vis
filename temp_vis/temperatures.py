def get_temperatures_by_points(temperature_data, x, y, z):
    result = list()
    count = 0

    x_len = len(x)
    for i in range(x_len):
        try:
            t = define_shell_temperature_by_interpolation(
                x[i], y[i], z[i], temperature_data
            )
        except IndexError:
            t = 0
        result.append(t)
        count += 1
        print(
            f'Vertices processed: {round(count / x_len * 100, 2)} %' + '\r',
            end=''
        )

    return result


def interpolation(t1, x1, t2, x2, x):
    t = (x - x1) * (t2 - t1) / (x2 - x1) + t1
    return t


def define_shell_temperature_by_interpolation(x, y, z, temps_arr):
    coordinates = (x, y, z)
    pre_arr_by_x = []
    for i in temps_arr:
        if (i[0][0] <= coordinates[0] < i[1][0]) or \
                (i[1][0] <= coordinates[0] < i[0][0]):
            pre_arr_by_x.append(i)
    pre_arr_by_y = []
    for i in pre_arr_by_x:
        if i[0][1] <= coordinates[1] < i[1][1]:
            pre_arr_by_y.append(i)
    pre_arr_by_z = []
    for i in pre_arr_by_y:
        if i[0][2] <= coordinates[2] < i[1][2]:
            pre_arr_by_z.append(i)
    t1 = pre_arr_by_z[0][2]
    t2 = pre_arr_by_z[0][3]
    y1 = pre_arr_by_z[0][0][1]
    y2 = pre_arr_by_z[0][1][1]
    y = coordinates[1]
    t = interpolation(t1, y1, t2, y2, y)
    return t
