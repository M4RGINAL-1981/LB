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
    return  (b - a) * np.mean(f(curva_x))

def MonteKarloSUM(a: int, b: int, f, N: int):
    if(int(N) <= int(1e8)):
        return MonteKarlo(a, b, f, N)
    sum = 0
    k = 1
    for i in range(int(1e8), int(N + 1e8), int(1e8)):
        print(f"Итерация №{k}")
        k += 1
        sum += MonteKarlo(a, b, f, int(1e8))
    return sum / (N / 1e8) 

def MonteKarloGeometric(a: int, b: int, c: int, d: int, f, N: int):
    curva_x = np.random.uniform(a, b, N)  # Получаем равномерное распределение по оси абцисс (От a до b)
    curva_y = np.random.uniform(c, d, N)  # Получаем равномерное распределение по оси ординат (От c до d)
    curva_G = curva_y <= f(curva_x) # Получаем массив булевых значений
    return (b - a) * (d - c) * np.mean(curva_G) # Ограничивающая площадь на k/N (np.mean(curva_G))


if __name__ == "__main__":
    A = -1
    B = 1
    C = 0
    D = 1
    N = int(1e11)
    f = F()

    start = time.time()

    print(f"A: {A}, B: {B}, f: {f}, N: {N}, S: {MonteKarloSUM(A, B, f, N)}")

    end = time.time()

    print(f"Прошло {round((end - start) / 3600, 2)} часа")
    #print(f"Ограничивающий прямоугольник: A: {A}, B: {B}, C: {C}, D: {D}. Функция: {f}. Кол-во точек N: {N}. Площадь: {MonteKarloGeometric(A, B, C, D, f, N)}")