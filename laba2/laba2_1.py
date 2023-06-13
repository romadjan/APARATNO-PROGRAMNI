import math

# Дані відповідно до 22 варіанту
Q_CHANGE_TEMP = 0.6
Q_MAX_TEMP = 4.5
T0_TEMP = 1
D_TEMP = 50

Q_CHANGE_TUSK = 0.5
Q_MAX_TUSK = 2.8
T0_TUSK = 0.1
D_TUSK = 25

# цей метод повертає значення Kx(To) відвовідно за формулою 2.9
def get_kx_t0(d, q_change, q_x):
    return (2 * d + math.pow(q_change, 2) - math.pow(q_x, 2)) / 2

# метод повертає список значень для певного параметра, який буде використвовуватись під час розрахунків
def get_list_of_value(parametr, tochnist):
    size = 5
    arr = []
    for i in range(size):
        if i % 2 == 0:
            arr.append(parametr + i / tochnist)
        else:
            arr.append(parametr - i / tochnist)
    arr.sort()
    return arr


def task_1():
    q_change_temp_list = get_list_of_value(Q_CHANGE_TEMP, 10)
    q_max_temp_list = get_list_of_value(Q_MAX_TEMP, 10)
    kx_temp = get_kx_t0(D_TEMP, Q_CHANGE_TEMP, Q_MAX_TEMP)
    delta_period_temp_list = get_list_of_value(T0_TEMP, 10)
    ktx_temp_t_delta_qh = [get_kx_t0(D_TEMP, x, Q_MAX_TEMP) for x in q_change_temp_list]
    ktx_temp_t_delta_qmax = [get_kx_t0(D_TEMP, Q_CHANGE_TEMP, x) for x in q_max_temp_list]

    q_change_tusk_list = get_list_of_value(Q_CHANGE_TUSK, 10)
    q_max_tusk_list = get_list_of_value(Q_MAX_TUSK, 10)
    kx_tusk = get_kx_t0(D_TUSK, Q_CHANGE_TUSK, Q_MAX_TUSK)

    delta_period_tusk_list = get_list_of_value(T0_TUSK, 50)
    ktx_press_t_delta_qh = [get_kx_t0(D_TUSK, x, Q_MAX_TUSK) for x in q_change_tusk_list]
    ktx_press_t_delta_qmax = [get_kx_t0(D_TUSK, Q_CHANGE_TUSK, x) for x in q_max_tusk_list]

    print("Визначення періоду опитування датчиків з реалізації випадкових процесів за температурою і тиском: \n")
    print("Величина Kx(T0) за температурою при заданих QxMax та Qh:")
    print(f"Kx(Ta) = {kx_temp:.2f}")
    print("Величина Kx(T0) за за тиском при заданих QxMax та Qh:")
    print(f"Kx(Ta) = {kx_tusk:.2f}\n")
    print("За графіками кореляційних функцій (див. рис. 2.3, 2.4), визначити значення періодів опитування Т0 датчиків температури і тиску:")
    print(f"T0 для датчика температури: {T0_TEMP:.2f}")
    print(f"T0 для датчика тиску: {T0_TUSK:.2f}\n")
    print("При постійній величині QxMax визначаємо декілька значень T0 при різних значеннях Qh для датчика температури:")
    print(f"Kx(T0) = {kx_temp:.2f}")
    print("QxMax = const")
    for i in range(len(delta_period_temp_list)):
        print(f"K(T - {i}) = {ktx_temp_t_delta_qh[i]:.4f}, T = {delta_period_temp_list[i]:.2f}")
    print()
    print("При постійній величині Qh визначаємо декілька значень T0 при різних значеннях QxMax для датчика температури:")
    print("Qh = const")
    for i in range(len(delta_period_temp_list)):
        print(f"K(T - {i}) = {ktx_temp_t_delta_qmax[i]:.4f}, T = {delta_period_temp_list[i]:.2f}")
    print()
    print("Датчик тиску:")
    print("Для постійної величини QxMax визначаємо декілька значень T0 при різних значеннях Qh:")
    print(f"Kx(T0) = {kx_tusk:.2f}")
    print("QxMax = const")
    for i in range(len(delta_period_tusk_list)):
        print(f"K(T - {i}) = {ktx_press_t_delta_qh[i]:.4f}, T = {delta_period_tusk_list[i]:.2f}")
    print()
    print("Для постійної величини Qh визначаємо декілька значень T0 при різних значеннях QxMax:")
    print("Qh = const")
    for i in range(len(delta_period_tusk_list)):
        print(f"K(T - {i}) = {ktx_press_t_delta_qmax[i]:.4f}, T = {delta_period_tusk_list[i]:.2f}")


if __name__ == "__main__": task_1()
