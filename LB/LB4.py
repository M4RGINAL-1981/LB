import numpy as np
import math
import matplotlib.pyplot as plt
import multiprocessing as mp
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


# Функция для worker должна быть на верхнем уровне
def worker_function(args):
    a_local, b_local, c_local, d_local, f_local, points = args
    return MonteKarloGeo(a_local, b_local, c_local, d_local, f_local, points)

def ParallelMonteCarloSUM(a: int, b: int, c: int, d: int, f, N: int, num_processes=4):
    if N <= int(1e8):
        return MonteKarloGeo(a, b, c, d, f, N)
    
    points_per_process = N // num_processes
    
    print(f"Параллельный расчет на {num_processes} процессах")
    print(f"Всего точек: {N:,}, на процесс: {points_per_process:,}")
    
    tasks = [(a, b, c, d, f, points_per_process) for _ in range(num_processes)]
    
    start_time = time.time()
    with mp.Pool(processes=num_processes) as pool:
        results = pool.map(worker_function, tasks)
    
    result = np.mean(results)
    print(f"Время расчета: {time.time() - start_time:.2f} сек")
    
    return result


def Print(N_values, Results_values, f):
    plt.figure(figsize=(8, 6))
    plt.plot(N_values, Results_values - f.S, linewidth=2, label='Cходимость')
    plt.plot(N_values, f.S, linewidth=2, label='Аналитическая площадь')

    plt.title(f"Анализ сходимости")
    plt.xlabel("N")
    plt.ylabel("Площадь A")
    plt.grid(True)
    plt.legend()
    plt.show()

def PrintTime(N_values, Time_values):
    plt.figure(figsize=(8, 6))
    plt.plot(N_values, Time_values, linewidth=2, label='Зависимость кол-во времени от кол-во точек')

    plt.title(f"Анализ сходимости")
    plt.xlabel("N")
    plt.ylabel("Кол-во времени")
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    A = -1
    B = 1
    C = 0
    D = 1
    N_values = [1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7, 1e8, 1e9]
    Time_values = []
    Results_values = []
    f = F()

    for i in range(len(N_values)):
        start = time.time()
        Results_values.append(ParallelMonteCarloSUM(A, B, C, D, f, N_values[i], num_processes=4))
        end = time.time()
        Time_values.append(round((end - start) / 60))
        
    Print(N_values, Results_values, f)
    PrintTime(N_values, Time_values)