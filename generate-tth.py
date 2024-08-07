import json
import os
import random
from datetime import datetime

os.makedirs('data/', exist_ok=True)


def generate_data():
    stations = {}
    start_date = datetime.now()

    for i in range(1, 10):
        stations[f'transformer_{i}'] = {
            'limit': random.randint(40, 60),
        }

    number = start_date.strftime('%d_%H_%M_%S')
    with open(f'data/tth_{number}.json', 'w') as f:
        json.dump(stations, f, indent=4)


if __name__ == '__main__':
    generate_data()
