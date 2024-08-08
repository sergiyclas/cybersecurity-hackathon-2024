import matplotlib.pyplot as plt
import numpy as np

# Години доби
hours = list(range(24))

# Функція для генерації швидкості вітру протягом доби
def generate_wind_speed(hours):
    # Припустимо, що швидкість вітру змінюється в залежності від часу доби
    # Вітровий графік може мати піки вранці та ввечері
    wind_speed = 5 + 3 * np.sin((np.array(hours) - 9) * np.pi / 12) ** 2
    return wind_speed

# Функція для генерації вироблення електроенергії на основі швидкості вітру
def generate_energy_output(wind_speed):
    # Вітровий генератор має функцію вироблення електроенергії, яка залежить від швидкості вітру
    # Вітрові турбіни зазвичай мають поріг запуску та максимальну швидкість
    power_output = np.where(wind_speed < 3, 0,  # Немає вироблення при швидкості < 3 м/с
                            np.where(wind_speed > 15,  # Вироблення на максимальному рівні при швидкості > 15 м/с
                                     5,
                                     (wind_speed - 3) * 0.5))  # Лінійна залежність між 3 і 15 м/с
    return power_output

# Генерація швидкості вітру
wind_speed = generate_wind_speed(hours)

# Генерація вироблення електроенергії
energy_output = generate_energy_output(wind_speed)

# Побудова графіку
plt.figure(figsize=(14, 8))

plt.plot(hours, wind_speed, label='Швидкість вітру (м/с)', color='blue', linestyle='--')
plt.plot(hours, energy_output, label='Вироблення електроенергії (кВт)', color='green')

plt.xlabel('Години доби')
plt.ylabel('Значення')
plt.title('Вироблення електроенергії вітровим генератором протягом доби')
plt.grid(True)
plt.legend()
plt.xticks(hours)
plt.tight_layout()
plt.show()
