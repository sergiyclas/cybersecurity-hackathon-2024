import json
import random
import os
from datetime import datetime, timedelta


os.makedirs('data/', exist_ok=True)

def generate_data():
    data = {}
    start_date = datetime.now()
    end_date = start_date + timedelta(days=10)
    current_date = start_date
    while current_date < end_date:
        hour = 0
        date_str = current_date.strftime('%Y-%m-%d')
        data[date_str] = dict()
        while hour <= 24:
            data[date_str][f'{hour}:00'] = {
                "users": {f"user_{i}": round(random.uniform(1, 2), 2) for i in range(1, 11)},
                "generations": {f"generation_{i}": round(random.uniform(3, 10), 2) for i in range(1, 6)}
            }
            hour += 1
        current_date += timedelta(hours=1)

    number = start_date.strftime('%d_%H_%M_%S')
    with open(f'data/historical_{number}.json', 'w') as f:
        json.dump(data, f, indent=4)
    with open(f'data/current_{number}.json', 'w') as f:
        json.dump(data, f, indent=4)


if __name__ == '__main__':
    generate_data()