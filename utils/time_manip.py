def mmss_2_ss(string):
    """
    mapping the format mm:ss.ms to ss.ms
    :param string:
    :return:
    """
    minute, second = string.split(':')
    return float(minute) * 60 + float(second)