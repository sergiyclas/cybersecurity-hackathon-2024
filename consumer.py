import matplotlib.pyplot as plt
import numpy as np

# Години доби
hours = list(range(24))


# Функція для генерації споживання електроенергії
def generate_energy_consumption(hours, peak_usage, morning_rise_peak, evening_fall_peak):
    # Основний рівень споживання
    base_usage = 0.3

    # Ранковий пік (з 06:00 до 09:00)
    morning_peak = np.maximum(0, np.sin((np.array(hours) - 6) * np.pi / 6)) ** 2 * morning_rise_peak
    print(morning_peak)

    # Вечірній пік (з 17:00 до 22:00)
    evening_peak = np.maximum(0, np.sin((np.array(hours) - 19) * np.pi / 5)) ** 2 * evening_fall_peak

    # Комбінація
    consumption = base_usage + morning_peak + evening_peak
    return consumption


# Витрати для приватного будинку
consumption_house = generate_energy_consumption(hours, peak_usage=1.5, morning_rise_peak=1.2, evening_fall_peak=1.8)

# Витрати для квартири (менше пікове споживання)
consumption_apartment = generate_energy_consumption(hours, peak_usage=1.0, morning_rise_peak=1.0, evening_fall_peak=1.2)

# Побудова графіку
plt.figure(figsize=(14, 8))

plt.plot(hours, consumption_house, label='Приватний будинок', color='blue')
plt.plot(hours, consumption_apartment, label='Квартира', color='green')

plt.xlabel('Години доби')
plt.ylabel('Витрати електроенергії (кіловат-години)')
plt.title('Витрати електроенергії для середньостатистичного жителя міста')
plt.grid(True)
plt.legend()
plt.xticks(hours)
plt.tight_layout()
plt.show()
