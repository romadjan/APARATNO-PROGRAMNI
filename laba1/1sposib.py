# алгоритм циклічного опитування датчиків
import random
import time

TIME_DELTA = 2
N = 10


class Sensor:
    def __init__(self, index, param_value, max_value, min_value, critical_delta, current_time):
        self.index = index
        self.param_value = param_value
        self.max_value = max_value
        self.min_value = min_value
        self.critical_delta = critical_delta
        self.current_time = current_time

    @classmethod
    def generate_random(cls, index, time_delta):
        index = index
        param_value = random.randint(-100, 100)
        max_value = random.randint(60, 95)
        min_value = random.randint(-95, -60)
        critical_delta = random.randint(1, 5)
        current_time = index * time_delta
        return cls(index, param_value, max_value, min_value, critical_delta, current_time)




def print_all_sensors_data(sensor):
    print(f"Датчик номер {sensor.index}: Значення датчика = {sensor.param_value}, Верхнє Граничне Значення = {sensor.max_value}, Нижнє Граничне Значення = {sensor.min_value}, Аварійне значення = {sensor.critical_delta}, Поточний час = {sensor.current_time}")


def check_sensor_validation(sensors):
    for sensor in sensors:
        max_delta = sensor.max_value - sensor.param_value
        min_delta = sensor.min_value - sensor.param_value
        if max_delta < 0:
            if abs(max_delta) > sensor.critical_delta:
                print('\033[91m!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\033[0m')
                print("\033[91mВерхнє Граничне Значення перевищено, показники є аварійними!\033[0m")
                print_all_sensors_data(sensor)
                print('\033[91m!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\033[0m\n')
            else:
                print(
                    f"\033[93mДатчик номер {sensor.index} - Верхнє Граничне Значення перевищено, але показники не є аварійними!\033[0m\n")
        elif min_delta > 0:
            if abs(min_delta) > sensor.critical_delta:
                print('\033[91m!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\033[0m')
                print("\033[91mЗначення менше Нижнього Граничного, показники є аварійними!\033[0m")
                print_all_sensors_data(sensor)
                print('\033[91m!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\033[0m\n')
            else:
                print(
                    f"\033[93mДатчик номер {sensor.index} - Значення менше Нижнього Граничного, але показники не є аварійними!\033[0m\n")
        else:
            print(f"\033[92mДатчик номер {sensor.index} - Показники в нормі!\033[0m\n")
        time.sleep(TIME_DELTA)


def cyclic_polling_of_sensors():
    sensors = [Sensor.generate_random(index, TIME_DELTA) for index in range(1, N + 1)]
    print('Дані по всим датчикам: \n')
    for sensor in sensors:
        print_all_sensors_data(sensor)
    print('\n')
    print('Запускаємо Аналіз даних Датчиків із періодом опитування в 2 секунди: \n')
    check_sensor_validation(sensors)
    print('\n')
    print('Кінець опитування!')


if __name__ == "__main__": cyclic_polling_of_sensors()
