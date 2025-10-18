import numpy as np
import multiprocessing
import matplotlib.pyplot as plt
import math

Square = math.pi / 2
Poins_count = 10 ** 7
Iterations_count = 100
Processes_count = 36


def monte_carlo_iteration():
    """
    Реализует метод Монте-Карло.
    Returns:
        s (float): посчитанная площадь
    """
    x = np.random.uniform(-1, 1, Poins_count)
    y = np.random.uniform(0, 1, Poins_count)
    points_check = x**2 + y**2 <= 1
    count = np.sum(points_check)
    s = 2 * count / Poins_count
    return s


def process(_):
    """
    Выполняет серию итераций одного процесса и собирает результаты нескольких итераций.
    Returns:
        result (list): список значений s для каждой итерации.
    """
    np.random.seed(42)
    result = []
    for _ in range(Iterations_count):
        s = monte_carlo_iteration()
        result.append(s)
    return result


def plot(N, S, S1, S2):
    """
    Строит график зависимости оценки площади от количества точек.
    Args:
        N (list): количества точек.
        S (list): средние значение площади.
        S1 (list): средние значение верхние границы.
        S2 (list): средние значение нижние границы.
    """
    plt.plot(N, S, marker='o', label='Посчитаная площадь')
    plt.plot(N, S1, marker='+', linestyle='--', label='Ошибка +')
    plt.plot(N, S2, marker='+', linestyle='--', label='Ошибка -')
    plt.axhline(Square, linestyle='--', label='Настоящая Площадь')
    plt.xscale('log')
    plt.xlabel('Количество точек')
    plt.ylabel('Площадь')
    plt.legend()
    plt.grid(True)
    plt.title('Зависимость оценки площади от количества точек')
    plt.show()

if __name__ == "__main__":

    with multiprocessing.Pool(Processes_count) as pool:
        Results = pool.map(process, range(Processes_count))

    Item = []
    for i in Results:
        for j in i:
            Item.append(j)

    N = []
    S = []
    S1 = []
    S2 = []

    Total_points = 0
    P_sum = 0

    for i in range(len(Item)):
        Total_points += Poins_count
        P_sum += Item[i]
        S_sum = P_sum / (i + 1)
        p = S_sum / 2
        sig = 2 * np.sqrt(p * (1 - p) / Total_points)

        N.append(Total_points)
        S.append(S_sum)
        S1.append(S_sum + sig)
        S2.append(S_sum - sig)

    plot(N, S, S1, S2)