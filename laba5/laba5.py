import math

SIGNAL = 10
Po = 2.8
Y_MAX = 16.39
ROZRAD = 12
F = 1024
T = 2048
P = 3072
F_MAX = 600


# проводимо обчислення фактичного значення температури
def compute_temp(output_signal, y_max, resolution, T):
    acp_max = pow(2, resolution)
    knp = output_signal / y_max
    y = (output_signal / (acp_max * knp)) * T
    return 3.01 + 13.75 * y - 0.03 * pow(y, 2)

# проводимо обчислення фактичного значення тиску
def compute_tusk(P, output_signal, resolution):
    acp_max = pow(2, resolution)
    return (P / acp_max) * output_signal


# проводимо обчислення фактичного значення затрат
def compute_spend(t, p, p0, F, f_max, resolution):
    acp_max = pow(2, resolution)
    pG = 1.2 - 0.013 * t + 0.72 * p + 0.000036 * pow(t, 2) + 0.0024 * pow(p, 2) - 0.0014 * t * p
    kp = math.sqrt(pG / p0)
    return math.sqrt(F / acp_max) * f_max * kp


if __name__ == "__main__":
    print(f"Дані згідно варіанту(варіант 22): \n"
          f"Перегрітий пар: {Po}\n"
          f"Максимальна кількість сигналів: {Y_MAX}\n"
          f"Розрядність АЦП: {ROZRAD}\n"
          f"Код АЦП для витрат: {F}\n"
          f"Код АЦП для тиску: {P}\n"
          f"Код АЦП для температури: {T}\n"
          f"Вихідний сигнал: {SIGNAL}\n")
    temp = compute_temp(SIGNAL, Y_MAX, ROZRAD, T)
    tusk = compute_tusk(P, SIGNAL, ROZRAD)
    spend = compute_spend(temp, tusk, Po, F, F_MAX, ROZRAD)
    print("Проведено обчислення фактичних значень вимірюваних величин:\n")
    print(f"Витрата: {spend}")
    print(f"Тиск: {tusk}")
    print(f"Температура: {temp}")


