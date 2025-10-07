import matplotlib.pyplot as plt
import numpy as np
from math import *

def f(x):
    return np.exp(-x) * np.sin(3*x)
def Task1(f, A: int, B: int, N: int):
    x = np.linspace(A, B, N)
    plt.figure(figsize=(8, 6))
    y = f(x)
    plt.plot(x, y, linewidth=2) 
    plt.title(f"График функции: [" + r"$e^{-x} \sin(3x)$" + "]")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    #plt.savefig(f"function_plot_2.png", dpi=300, bbox_inches='tight')
    plt.close()
def g(x):
    return np.sqrt(x)
def u(x):
    return x
def v(x):
    return np.log10(x + 1)
def Task2(g, u, v, A: int, B: int, N: int):
    x = np.linspace(A, B, N)
    plt.figure(figsize=(8, 6))

    g_x = g(x)
    u_x = u(x)
    v_x = v(x)

    plt.plot(x, g_x, color='red', label='$\sqrt{x}$') 
    plt.plot(x, u_x, color='blue', label='$x$') 
    plt.plot(x, v_x, color='green', label='$\log_{10}(x+1)$')
    
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.legend()
    #plt.savefig(f"function_plot_21.png", dpi=300, bbox_inches='tight')
    plt.close()
def Task3(a: float, b: float, sigma: float, A: int, B: int, N: int):
    x = np.random.uniform(A, B, N)
    epsilon = np.random.normal(0, sigma, N)
    y = a * x + b + epsilon
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, alpha=0.6, label='Данные')

    x_line = np.linspace(A, B, 100)
    y_line = a * x_line + b
    plt.plot(x_line, y_line, 'r--', linewidth=2, label='Модель')
    
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title(f'Точечный график с линией регрессии\ny = {a}x + {b} + ε, где ε ~ N(0, {sigma})')
    plt.grid(True, alpha=0.3)
    plt.legend()

    #plt.savefig(f"function_plot_21.png", dpi=300, bbox_inches='tight')

    plt.show()
def Task4():
    #products = ['Диапозон 1', 'Диапозон 2', 'Диапозон 3', 'Диапозон 4',  'Диапозон 5']
    #sales = [R1, R2, R3, R4, R5]
    pass
def Task5():
    pass
def fZ6(x, a:float):
    return x**a
def gZ6(x, b:float):
    return np.exp(b * x)
def Task6(fZ6, gZ6, a: float, b: float, A: int, B: int, N: int):
    x = np.linspace(A, B, N)
    fZ6_x = fZ6(x, a)
    gZ6_x = gZ6(x, b)


    plt.figure(figsize=(10, 6))


    plt.plot(x, fZ6_x, color="red", linewidth=2, label='f(x)')
    plt.plot(x, gZ6_x, color="blue", linewidth=2, label='g(x)')
    
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.yscale('log')

    plt.title(f'График f(x) и g(x)')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.show()

def cos_exp(x):
    return np.cos(x) + np.exp(x * -0.2)

def Task7():
    x = np.linspace(0, 10, 100)
    y = cos_exp(x)
    y1 = 0
    plt.plot(x, y)
    plt.xlabel("x") 
    plt.ylabel("y") 
    plt.grid()     
    plt.fill_between(x, y, y1, where=y > y1, alpha = 0.3, color = "green", label = "y > 0")
    plt.fill_between(x, y, y1, where=y < y1, alpha = 0.3, color = "red", label = "y < 0")
    plt.legend()
    plt.show()
def Task8():
    N = [10, 100, 1000, 10000, 100000]
    error_A = [0.1, 0.03, 0.01, 0.003, 0.001]
    error_B = [0.1, 0.05, 0.025, 0.012, 0.006]

    plt.loglog(N, error_B)
    plt.loglog(N, error_A)
    plt.show()
def Task9():
    dots = np.linspace(2, 3, 5000 * 0.7) + np.linspace(6, 7, 5000 * 0.3)
    plt.hexbin(dots)
    plt.show()


    # Генерация данных
    np.random.seed(42)  # для воспроизводимости результатов

    # Количество точек для каждого распределения
    n_points_1 = int(5000 * 0.7)  # 70% = 3500 точек
    n_points_2 = 5000 - n_points_1  # 30% = 1500 точек

    # Параметры распределений
    mu1 = np.array([2, 3])  # μ₁ = (2,3)
    mu2 = np.array([6, 7])  # μ₂ = (6,7)
    sigma = np.eye(2)       # Σ = I (единичная матрица)

    # Генерация точек из первого распределения N(μ₁, I)
    points1 = np.random.multivariate_normal(mu1, sigma, n_points_1)

    # Генерация точек из второго распределения N(μ₂, I)
    points2 = np.random.multivariate_normal(mu2, sigma, n_points_2)

    # Объединение всех точек
    all_points = np.vstack([points1, points2])

    # Разделение на координаты X и Y
    x = all_points[:, 0]
    y = all_points[:, 1]

    # Создание гексагональной карты плотности
    plt.figure(figsize=(10, 8))
    hexbin_plot = plt.hexbin(x, y, gridsize=30, cmap='Blues', alpha=0.8)

    # Добавление цветовой шкалы
    colorbar = plt.colorbar(hexbin_plot)
    colorbar.set_label('Плотность точек')

    # Подписи осей
    plt.xlabel('X')
    plt.ylabel('Y')

    # Заголовок
    plt.title('Гексагональная карта плотности точек')

    # Отображение сетки для лучшей читаемости
    plt.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()

    # Дополнительная информация о данных
    print(f"Общее количество точек: {len(all_points)}")
    print(f"Точек из N(μ₁): {n_points_1}")
    print(f"Точек из N(μ₂): {n_points_2}")
    print(f"Диапазон X: [{x.min():.2f}, {x.max():.2f}]")
    print(f"Диапазон Y: [{y.min():.2f}, {y.max():.2f}]")
def Task10():
    '''- Группа A: 𝑁(70,10), 100 точек
    - Группа B: 𝑁(75,5)
    - Группа C: Uniform[50,90]
    Задача:
    - Постройте “скрипичные” диаграммы (violin plot) для трёх групп
    - Подпишите оси
    - Заголовок: "Сравнение распределений оценок"
    - Сравните с boxplot (в отчёте)
    '''
    np.random.seed(42)

    n_dots = 100
    A = np.random.normal(70, 10, n_dots)
    B = np.random.normal(75, 5, n_dots)
    C = np.random.uniform(50, 90, n_dots)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

    ax1.violinplot([A, B, C], showmeans= True, showmedians= True)
    ax1.set_title("Сравнение рапределений оценок violin plot")
    ax1.set_ylabel("Оценки")
    ax1.set_xticks([1, 2, 3])
    ax1.set_xticklabels(['Группа A\nN(70,10)', 'Группа B\nN(75,5)', 'Группа C\nUniform[50,90]'])
    ax1.grid(True, alpha = 0.3)

    ax2.boxplot([A, B, C])
    ax2.set_title("Сравнение рапределений оценок boxplot")
    ax2.set_xticks([1, 2, 3])
    ax2.set_xticklabels(['Группа A\nN(70,10)', 'Группа B\nN(75,5)', 'Группа C\nUniform[50,90]'])
    ax2.set_ylabel("Оценки")
   
    plt.tight_layout()
    plt.show()

def Task11():
    pass

def Task12():
    pass

def Task13():
    pass

def Task14():
    pass

def Task15():
    pass
    

if __name__ == "__main__":
    #Task1(f, 0, 6, 500)
    #Task2(g, u, v, 1e-10, 6, 500)
    #Task3(2, 3, 2, 0, 10, 200)
    #Task4()  Не реализовано
    #Task5()  Не реализовано
    #Task6(fZ6, gZ6, 1, 0.2, 1, 50, 1000)
    Task7()
    Task8()
    Task9()
    Task10()
    Task11()
    Task12()
    Task13()
    Task14()
    Task15()