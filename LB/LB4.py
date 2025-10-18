import numpy as np
import multiprocessing
import matplotlib.pyplot as plt
import math

class F:
    def __init__(self):
        pass
    def __call__(self, x: float):
        return np.sqrt(1 - np.pow(x, 2))

Square = math.pi / 2
Poins_count = 10 ** 7
Iterations_count = 100
Processes_count = multiprocessing.cpu_count()

f = F()

A = -1
B = 1
C = 0
D = 1


def monte_carlo_iteration(iteration_seed):
    """
    Реализует метод Монте-Карло.
    Returns:
        s (float): посчитанная площадь
    """
    rng = np.random.default_rng(iteration_seed)
    x = np.random.uniform(A, B, Poins_count)
    y = np.random.uniform(C, D, Poins_count)
    points_check = y <= f(x)
    return (B - A)*(D - C) * np.mean(points_check)

def process(process_id):
    """
    Выполняет серию итераций одного процесса и собирает результаты нескольких итераций.
    Returns:
        result (list): список значений s для каждой итерации.
    """
    result = []
    base_seed = process_id * Iterations_count
    for i in range(Iterations_count):
        iteration_seed = base_seed + i
        s = monte_carlo_iteration(iteration_seed)
        result.append(s)
    return result


def plot(N, S, S1, S2):
    """
    Строит график зависимости оценки площади от количества точек.
    Args:
        N  (list): количества точек.
        S  (list): средние значение площади.
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
        p = S_sum / ((B - A)*(D - C))
        sig = (B - A)*(D - C) * np.sqrt(p * (1 - p) / Total_points)

        N.append(Total_points)
        S.append(S_sum)
        S1.append(S_sum + sig)
        S2.append(S_sum - sig)

    print(f"Точная площадь: {Square:.6f}")
    print(f"Вычисленная площадь: {S[-1]:.6f}")
    print(f"Относительная ошибка: {abs(S[-1]-Square)/Square*100:.4f}%")
    
    plot(N, S, S1, S2)