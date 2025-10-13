import numpy as np
import multiprocessing as mp
import time 

class F:
    def __call__(self, x):
        return np.sqrt(1 - x**2)
    
    def __str__(self):
        return "sqrt(1 - x**2)"
    
def MonteKarlo(a: int, b: int, f, N: int):
    curva_x = np.random.uniform(a, b, N)
    return (b - a) * np.mean(f(curva_x))

# Функция для worker должна быть на верхнем уровне
def worker_function(args):
    a_local, b_local, f_local, points = args
    return MonteKarlo(a_local, b_local, f_local, points)

def ParallelMonteCarloSUM(a: int, b: int, f, N: int, num_processes=4):
    if N <= int(1e8):
        return MonteKarlo(a, b, f, N)
    
    points_per_process = N // num_processes
    
    print(f"Параллельный расчет на {num_processes} процессах")
    print(f"Всего точек: {N:,}, на процесс: {points_per_process:,}")
    
    tasks = [(a, b, f, points_per_process) for _ in range(num_processes)]
    
    start_time = time.time()
    with mp.Pool(processes=num_processes) as pool:
        results = pool.map(worker_function, tasks)
    
    result = np.mean(results)
    print(f"Время расчета: {time.time() - start_time:.2f} сек")
    
    return result

def MonteKarloGeometric(a: int, b: int, c: int, d: int, f, N: int):
    curva_x = np.random.uniform(a, b, N)
    curva_y = np.random.uniform(c, d, N)
    curva_G = curva_y <= f(curva_x)
    return (b - a) * (d - c) * np.mean(curva_G)

if __name__ == "__main__":
    A = -1
    B = 1
    C = 0
    D = 1
    N = int(1e9)
    f = F()

    start = time.time()

    result = ParallelMonteCarloSUM(A, B, f, N, num_processes=4)
    
    end = time.time()

    print(f"A: {A}, B: {B}, f: {f}, N: {N}")
    print(f"S: {result}")
    print(f"Прошло {round((end - start) / 60, 2)} минут")