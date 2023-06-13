import numpy as np
# константи згідно до варіанту
X1 = 12.2
X2 = 11.8
X3 = 12.3
X4 = 34.3
L = 1.6
S1 = 0.3
S2 = 0.2
S3 = 0.35
S4 = 0.33
DEL_X = 0.45
DEL_X_4 = 0.65

# Визначаємо похибку l
def get_coef_l(x_list):
    return x_list[0] + x_list[1] + x_list[2] - x_list[3]

# знайдемо числові значення коефіцієнтів а
def get_coef_a(l, x_list):
    return [1 if l / x > 0 else -1 for x in x_list]


def get_delta_q(coef_a, x_list):
    return [x * a for x, a in zip(x_list, coef_a)]

# розрахуємо вагові коефіцієнти р
def get_coef_p(s_list):
    k = 1 / ((1 / s_list[0]) + (1 / s_list[1]) + (1 / s_list[2]) + (1 / s_list[3]))
    return [k / s for s in s_list]


# Запис системи рівнянь
def get_result_system(coef_p, del_q, coef_l):
    system = (
        (2 * coef_p[0] * del_q[0], 0, 0, 0, 1),
        (0, 2 * coef_p[1] * del_q[1], 0, 0, 1),
        (0, 0, 2 * coef_p[2] * del_q[2], 0, 1),
        (0, 0, 0, 2 * coef_p[3] * del_q[3], 1),
        (del_q[0], del_q[1], del_q[2], -del_q[3], 0)
    )
    base = [0, 0, 0, 0, coef_l]
    res = np.linalg.solve(system, base)
    return res[1:]


# розраховуємо скориговані оцінки значень вимірюваних величин
def get_res(x_list, del_q):
    return (x_list[0] - del_q[0], x_list[1] - del_q[1], x_list[2] - del_q[2], x_list[3] + abs(del_q[3]))

if __name__ == "__main__":
    print(f"Виведемо всі константи згідно аріанту(22 варіант):\n"
          f"x1: {X1}\n"
          f"x2: {X2}\n"
          f"x3: {X3}\n"
          f"x4: {X4}\n"
          f"l: {L}\n"
          f"del x1: {DEL_X}\n"
          f"del x2: {DEL_X}\n"
          f"del x3: {DEL_X}\n"
          f"del x4: {DEL_X_4}\n"
          f"σ1: {S1}\n"
          f"σ2: {S2}\n"
          f"σ3: {S3}\n"
          f"σ4: {S4}\n")
    x_list = (X1, X2, X3, X4)
    s_in_kvadrat_list = [s ** 2 for s in (S1, S2, S3, S4)]
    del_x_list = (DEL_X, DEL_X, DEL_X, DEL_X_4)
    coef_l = get_coef_l(x_list)
    print(f"Визначаємо похибку l: {coef_l}")
    no_error = abs(coef_l) < L
    if not no_error:
        print(f"|{abs(coef_l)}| > {L}")
        print('Умова не виконується потрібно відкоригувати значення:\n')
        coef_a_list = get_coef_a(L, x_list)
        delta_q = get_delta_q(coef_a_list, x_list)
        p_coefficients = get_coef_p(s_in_kvadrat_list)
        print(f"Запишемо систему рівнянь для цього спочатку розрахуємо вагові коефіцієнти р: {p_coefficients}")
        systema = get_result_system(p_coefficients, delta_q, coef_l)
        print(f"Запис системи: {systema}")
        result = get_res(x_list, systema)
        print("Відкориговані значення:")
        print("q1:", result[0])
        print("q2:", result[1])
        print("q3:", result[2])
        print("q4:", result[3])
        print(f"Проведемо перевірку похибка l = {get_coef_l(result)}, що є менше за {L}")

    else:
        print(f'Похибка в межах норми {abs(coef_l)} < {L}')
