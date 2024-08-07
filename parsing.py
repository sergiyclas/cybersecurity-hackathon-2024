import json

def parser_current(path: str, COUNT_HOURS, CURRENT_HOUR, CURRENT_DAY):
    with open(path, 'r') as file:
        data = json.load(file)
        needed_data = {}
        for i in range(1):
            hour = str(CURRENT_HOUR + i) + ':00'
            needed_data[CURRENT_HOUR + i] = data[CURRENT_DAY][hour]

    return needed_data


def parser_historical(path: str, COUNT_HOURS, CURRENT_HOUR, CURRENT_DAY):
    CURRENT_DAY = '2023' + CURRENT_DAY[4:]
    with open(path, 'r') as file:
        data = json.load(file)
        needed_data = {}
        for i in range(COUNT_HOURS):
            hour = str(CURRENT_HOUR + i) + ':00'
            needed_data[CURRENT_HOUR + i] = data[CURRENT_DAY][hour]

    return needed_data


def parser_weather(path: str, COUNT_HOURS, CURRENT_HOUR, CURRENT_DAY):
    with open(path, 'r') as file:
        data = json.load(file)
        needed_data = {}
        for i in range(COUNT_HOURS):
            hour = str(CURRENT_HOUR + i) + ':00'
            needed_data[CURRENT_HOUR + i] = data[CURRENT_DAY][hour]

    return needed_data