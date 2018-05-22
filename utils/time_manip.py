def mmss_2_ss(string, fmt=0):
    """
    mapping the format mm:ss.ms to ss.ms
    :param string:
    :param fmt
    :return:
    """
    print(string)
    if fmt == 0:
        minute, second = string.split(':')
    elif fmt == 1:
        minute, second, decimal = string.split(':')
        second = second + '.' + decimal
    else:
        raise ValueError("fmt is not valid.")
    return float(minute) * 60 + float(second)