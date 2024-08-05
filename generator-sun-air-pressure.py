import json
import os
import random
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
                "SES": {f"ses_{i}": round(random.uniform(1, 2), 2) for i in range(1, 11)},
                "WES": {f"wes_{i}": round(random.uniform(3, 10), 2) for i in range(1, 6)}
            }
            hour += 1
        current_date += timedelta(hours=1)

    number = current_date.strftime('%d_%H_%M_%S')
    with open(f'data/predict_weather_{number}.json', 'w') as f:
        json.dump(data, f, indent=4)


if __name__ == '__main__':
    generate_data()
