def parser_data(path: str):
    with open(path, 'r') as file:
        data = json.load(file)
        needed_data = {}
        for i in range(COUNT_HOURS):
            hour = str(CURRENT_HOUR + i) + ':00'
            needed_data[CURRENT_HOUR + i] = data[CURRENT_DAY][hour]

    return needed_data
