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
        date_str = current_date.strftime('2023-%m-%d')
        data[date_str] = dict()
        while hour <= 24:
            data[date_str][f'{hour}:00'] = {
                "CONSUMERS": {f"consumer_{i}": round(random.uniform(0.5, 12), 2) for i in range(1, 52)},
                "SES": {f"ses_{i}": round(random.uniform(24 - hour + 0.5 if hour > 12 - 0.5 else hour, 24 - hour - 0.5 if hour > 12 else hour + 0.5), 2) for i in range(1, 19)},
                "WES": {f"wes_{i}": round(random.uniform(0, 8), 2) for i in range(1, 13)},

            }
            hour += 1
        current_date += timedelta(hours=1)
    #
    number = start_date.strftime('%d_%H_%M_%S')
    with open(f'data/historical.json', 'w') as f:
         json.dump(data, f, indent=4)


if __name__ == '__main__':
    generate_data()
