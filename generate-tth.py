import json
import os
import random
from datetime import datetime

os.makedirs('data/', exist_ok=True)


def generate_data():
    stations = {}
    start_date = datetime.now()

    for i in range(random.randint(10, 10)):
        stations[f'station_{i}'] = {
            'limit': random.randint(1, 10),
        }

    number = start_date.strftime('%d_%H_%M_%S')
    with open(f'data/tth_{number}.json', 'w') as f:
        json.dump(stations, f, indent=4)


if __name__ == '__main__':
    generate_data()
