import json
import os
import random
from datetime import datetime

os.makedirs('data/', exist_ok=True)

wes_list = [f'wes_{i}' for i in range(10)]
ses_list = [f'ses_{i}' for i in range(10)]
custom_list = [f'customer_{i}' for i in range(10)]
wes_rand = list(range(10))
ses_rand = list(range(10))
custom_rand = list(range(10))
random.shuffle(wes_rand)
random.shuffle(ses_rand)
random.shuffle(custom_rand)
print(wes_rand)


def generate_data():
    stations = {}
    start_date = datetime.now()

    for i in range(random.randint(10, 10)):
        stations[f'station_{i}'] = {
            'limit': random.randint(1, 10),
            'dependecies': [f'{ses_list[ses_rand[i]]}',
                            f'{wes_list[wes_rand[i]]}',
                            f'{custom_list[custom_rand[i]]}']
        }

    number = start_date.strftime('%d_%H_%M_%S')
    with open(f'data/tth_{number}.json', 'w') as f:
        json.dump(stations, f, indent=4)


if __name__ == '__main__':
    generate_data()
