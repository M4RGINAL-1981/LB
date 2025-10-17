import numpy as np
import math
import matplotlib.pyplot as plt
import multiprocessing
import time 

class F:
    def __call__(self, x):
        return np.sqrt(1 - x**2)
    
    def S(self):
        return math.pi / 2
    
    def __str__(self):
        return "sqrt(1 - x**2)"
    

def MonteKarloGeo(a: int, b: int, c: int, d: int, f, N: int):
    curva_x = np.random.uniform(a, b, N)
    curva_y = np.random.uniform(c, d, N)
    curva_G = curva_y <= f(curva_x)
    return (b - a) * (d - c) * np.mean(curva_G)

def process(a: int, b: int, c: int, d: int, f, N: int):
    """
    Выполняет серию итераций одного процесса и собирает результаты нескольких итераций.
    Returns:
        result (list): список значений s для каждой итерации.
    """
    np.random.seed(42)
    if(N < 1e8):
        return MonteKarloGeo(a, b, c, d, f, N)
    else:     
        result = []
        for _ in range(int(1e8), int(N + 1e8), int(1e8)):
            s = MonteKarloGeo(a, b, c, d, f, int(1e8))
            result.append(s)
        return result


def plot(N, S, S1, S2, f):
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
    plt.axhline(f.S(), linestyle='--', label='Настоящая Площадь')
    plt.xscale('log')
    plt.xlabel('Количество точек')
    plt.ylabel('Площадь')
    plt.legend()
    plt.grid(True)
    plt.title('Зависимость оценки площади от количества точек')
    plt.show()


if __name__ == "__main__":
    A = -1
    B = 1
    C = 0
    D = 1
    Processes_count = 36
    N_values = 1e8
    Time_values = []
    Results_values = []
    f = F()

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

    P_sum = 0

    for i in range(len(Item)):
        P_sum += Item[i]
        S_sum = P_sum / (i + 1)
        p = S_sum / 4
        sig = 4 * np.sqrt(p * (1 - p) / N_values)

        N.append(N_values)
        S.append(S_sum)
        S1.append(S_sum + sig)
        S2.append(S_sum - sig)

    plot(N, S, S1, S2, f)
