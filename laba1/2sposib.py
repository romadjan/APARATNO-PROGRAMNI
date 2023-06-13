# адресне опитування датчиків оператор може обрати датчик
import random
import time

DATA = [
    {
        'time_deltas': [5, 3, 4, 2, 7],
        'priority': [0, 5, 1, 2, 3]
    },
    {
        'time_deltas': [4, 2, 8, 12, 6],
        'priority': [5, 0, 3, 1, 4]
    },
    {
        'time_deltas': [2, 7, 4, 8, 3],
        'priority': [1, 2, 3, 4, 0]
    },
    {
        'time_deltas': [5, 6, 7, 2, 16],
        'priority': [0, 3, 5, 2, 7]
    },
    {
        'time_deltas': [6, 7, 3, 8, 4],
        'priority': [2, 5, 1, 0, 4]
    },
]
N = 5


class Sensor:
    def __init__(self, index, param_value, max_value, min_value, critical_delta, current_time, priority):
        self.index = index
        self.param_value = param_value
        self.max_value = max_value
        self.min_value = min_value
        self.critical_delta = critical_delta
        self.current_time = current_time
        self.priority = priority

    @classmethod
    def generate_random(cls, index, time_delta, priority):
        index = index
        param_value = random.randint(-100, 100)
        max_value = random.randint(60, 95)
        min_value = random.randint(-95, -60)
        critical_delta = random.randint(1, 5)
        current_time = time_delta
        priority = priority
        return cls(index, param_value, max_value, min_value, critical_delta, current_time, priority)


def print_all_sensors_data(sensor):
    print(
        f"Датчик номер {sensor.index}: Значення датчика = {sensor.param_value}, Верхнє Граничне Значення = {sensor.max_value}, Нижнє Граничне Значення = {sensor.min_value}, Аварійне значення = {sensor.critical_delta}, Період обстеження = {sensor.current_time}, Пріоритет = {sensor.priority}")


def get_user_input_variant(message):
    user_input = input(message)
    try:
        value = int(user_input)
        if value in range(1, N+1):
            return value
        else:
            print("Неіснуючий варіант!\n")
    except ValueError:
        if user_input != 'exit':
            print("Неіснуюча команда!\n")
    return user_input


def get_user_input(message):
    user_input = input(message)
    try:
        value = int(user_input)
        return value
    except ValueError:
        if user_input not in ("run", "exit"):
            print("Неіснуюча команда!\n")
        return user_input


def sensor_by_index(sensors, index):
    for sensor in sensors:
        if sensor.index == index:
            return sensor


def check_sensor_validation(sensors):
    for sensor in sensors:
        time.sleep(sensor.current_time)
        max_delta = sensor.max_value - sensor.param_value
        min_delta = sensor.min_value - sensor.param_value
        if max_delta < 0:
            if abs(max_delta) > sensor.critical_delta:
                print('\033[91m!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\033[0m')
                print("\033[91mВерхнє Граничне Значення перевищено, показники є аварійними!\033[0m")
                print_all_sensors_data(sensor)
                print('\033[91m!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\033[0m\n')
            else:
                print(f"\033[93mДатчик номер {sensor.index} - Верхнє Граничне Значення перевищено, але показники не є аварійними!\033[0m")
                print_all_sensors_data(sensor)
                print('\n')
        elif min_delta > 0:
            if abs(min_delta) > sensor.critical_delta:
                print('\033[91m!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\033[0m')
                print("\033[91mЗначення менше Нижнього Граничного, показники є аварійними!\033[0m")
                print_all_sensors_data(sensor)
                print('\033[91m!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\033[0m\n')
            else:
                print(f"\033[93mДатчик номер {sensor.index} - Значення менше Нижнього Граничного, але показники не є аварійними!\033[0m")
                print_all_sensors_data(sensor)
                print('\n')
        else:
            print(f"\033[92mДатчик номер {sensor.index} - Показники в нормі!\033[0m")
            print_all_sensors_data(sensor)
            print('\n')


def check_sensor_by_id(sensor):
    time.sleep(sensor.current_time)
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
                f"\033[93mДатчик номер {sensor.index} - Верхнє Граничне Значення перевищено, але показники не є аварійними!\033[0m")
            print_all_sensors_data(sensor)
            print('\n')
    elif min_delta > 0:
        if abs(min_delta) > sensor.critical_delta:
            print('\033[91m!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\033[0m')
            print("\033[91mЗначення менше Нижнього Граничного, показники є аварійними!\033[0m")
            print_all_sensors_data(sensor)
            print('\033[91m!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\033[0m\n')
        else:
            print(
                f"\033[93mДатчик номер {sensor.index} - Значення менше Нижнього Граничного, але показники не є аварійними!\033[0m")
            print_all_sensors_data(sensor)
            print('\n')
    else:
        print(f"\033[92mДатчик номер {sensor.index} - Показники в нормі!\033[0m")
        print_all_sensors_data(sensor)
        print('\n')


def run_program(sensors):
    for sensor in sensors:
        print_all_sensors_data(sensor)
    while True:
        print('\n')
        print("Щоб отримати дані з певного латчика введіть його індекс в поле вводу")
        print('Щоб запустити програму автоматично, тобто вивести інформацію по всим датчикам відповідно до пріоритетів, в поле вводу введіть "run" ')
        print('Щоб закінчити роботу програми в поле вводу введіть "exit"\n')

        user_input = get_user_input("Поле вводу: ")

        if type(user_input) is str:
            if user_input == "exit":
                break
            if user_input == "run":
                sensors = sorted(sensors, key=lambda obj: obj.priority)
                check_sensor_validation(sensors)
                continue

        if type(user_input) is int:
            if user_input in range(1, N + 1):
                check_sensor_by_id(sensor_by_index(sensors, user_input))
            else:
                print("Датчик з таким індексом не існує!\n")


def cyclic_polling_of_sensors():
    print("Старт програми:")
    variant = get_user_input_variant("Виберіть варіант з даними(від 1 до 5) або введіть 'exit' для зупинки програми: ")
    if variant and variant != 'exit':
        time_deltas = DATA[variant - 1].get('time_deltas')
        priorities = DATA[variant - 1].get('priority')
        sensors = [Sensor.generate_random(index, time_deltas[index - 1], priorities[index - 1]) for index in
                   range(1, N + 1)]
        print(f" Пріоритетність: {priorities}")
        print(f" Період обстеження: {time_deltas}\n")
    while True:
        if variant == 'exit':
            break
        if not isinstance(variant, int):
            continue
        run_program(sensors)
        break


if __name__ == "__main__": cyclic_polling_of_sensors()
