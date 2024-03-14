def init_log(path):
    """
    Ininitial logs file with path parameter.
    """
    file = open(path, 'w+')
    file.close()


def reten_log(path):
    """
    Try to truncate logs file when logs file has lines more then 200 lines.
    """
    with open(path, 'r+') as file:
        lines = file.readlines()
        if len(lines) > 200:
            file.seek(0)
            file.truncate()
