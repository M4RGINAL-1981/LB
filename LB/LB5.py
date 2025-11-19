import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def function_1(x):
    """
    Вычисляет значение функции f(x) = x³ - 6x² + 9x
    """
    return x**3 - 6*x**2 + 9*x

def chart_1():
    """
    Строит график функции f(x) = x³ - 6x² + 9x
    """
    x_arr = np.linspace(-1,5,500)
    y_arr = function_1(x_arr)
    plt.plot(x_arr, y_arr)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('График функции: $x^3 - 6x^2 + 9x$')
    plt.grid(True)
    plt.savefig('function_plot_13.png')
    plt.show()

def function_2_1(x):
    """
    Вычисляет значение функции f(x) = x³
    """
    return x**3

def function_2_2(x):
    """
    Вычисляет значение функции f(x) = 3x²
    """
    return 3*x**2

def function_2_3(x):
    """
    Вычисляет значение функции f(x) = 9x
    """
    return 9*x

def chart_2():
    """
    Строит три функции на одном графике с разными стилями линий
    """
    x_arr = np.linspace(-1,5,500)
    y1_arr = function_2_1(x_arr)
    y2_arr = function_2_2(x_arr)
    y3_arr = function_2_3(x_arr)
    plt.plot(x_arr, y1_arr, label='$x^3$', color='blue', linestyle='dotted')
    plt.plot(x_arr, y2_arr, label='$3x^2$', color='red', linestyle='dashed')
    plt.plot(x_arr, y3_arr, label='$9x$', color='green', linestyle='solid')
    plt.xlabel('x')
    plt.ylabel('Значение функции')
    plt.legend(loc='best')
    plt.title('Три функции на одном графике')
    plt.grid(True)
    plt.show()

def chart_3():
    """
    Создает точечный график с линейной регрессией
    """
    a = 2
    b = 3
    sig = 2
    x_arr = np.random.uniform(0, 10, 200)
    es = np.random.normal(0, sig, 200)
    y_arr = a * x_arr + b + es
    plt.scatter(x_arr, y_arr, alpha=0.6, label='Данные')
    x_line = np.linspace(0, 10, 100)
    y_line = a * x_line + b
    plt.plot(x_line, y_line, '--', label='Модель')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(loc='best')
    plt.title('Точечный график с линией регрессии')
    plt.show()
    
def chart_4():
    """
    Создает столбчатую диаграмму и круговую диаграмму для визуализации распределения данных
    """
    products = ['Диапазон 1', 'Диапазон 2', 'Диапазон 3', 'Диапазон 4', 'Диапазон 5']
    sales = [10, 20, 15, 30, 25]
    colors = ['blue', 'orange', 'green', 'red', 'purple']
    
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(products, sales, color=colors)
    
    ax.bar_label(bars, labels=[str(v) for v in sales], padding=1)
    
    ax.set_xlabel('Диапазоны')
    ax.set_ylabel('Максимальный размах')
    ax.set_title('Столбчатая диаграмма размахов по диапазонам')
    plt.show()

    
    explode = [0, 0, 0, 0.5, 0]

    plt.figure(figsize=(8, 8))
    plt.pie(sales, labels=products, autopct='%1.1f%%', colors=colors, explode=explode)
    plt.title('Распределение размахов по диапазонам')
    plt.show()

    
def chart_5():
    """
    Создает компоновку из 4 графиков для отображения всех функций
    """
    x_arr = np.linspace(-1,5,500)
    y1_arr = function_2_1(x_arr)
    y2_arr = function_2_2(x_arr)
    y3_arr = function_2_3(x_arr)
    y4_arr = function_1(x_arr)
    
    plt.figure(figsize=(12, 10))
    plt.suptitle('Функции из варианта 13', fontsize=16)
    
    plt.subplot(2, 2, 1)
    plt.plot(x_arr, y1_arr)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('График: $x^3$')

    plt.subplot(2, 2, 2)
    plt.plot(x_arr, y2_arr)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('График: $3x^2$') 

    plt.subplot(2, 2, 3)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.plot(x_arr, y3_arr)
    plt.title('График: $9x$') 

    plt.subplot(2, 2, 4)
    plt.plot(x_arr, y4_arr)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('График: $x^3 - 6x^2 + 9x$')

    plt.show()
    
def chart_6():
    """
    Сравнивает степенную и экспоненциальную функции в логарифмическом масштабе
    """
    a = 13 / 2  
    b = 13 / 10  
    x_arr = np.linspace(1, 50, 500)

    y1_arr = x_arr ** a
    y2_arr = np.exp(b * x_arr)

    plt.plot(x_arr, y1_arr, label='x_arr ** a')
    plt.plot(x_arr, y2_arr, label='np.exp(b * x_arr)')
    plt.yscale('log')
    plt.xlabel('x')
    plt.ylabel('Значение функции')
    plt.title('Функции для варианта 13 с логарифмической шкалой y')
    plt.legend()
    plt.show()

def chart_7():
    """
    Визуализирует области положительных и отрицательных значений функции
    """
    x_arr = np.linspace(-1, 5, 500)
    y_arr = function_1(x_arr)

    plt.figure(figsize=(10, 6))
    plt.plot(x_arr, y_arr, color='blue', linewidth=2, label='$f(x) = x^3 - 6x^2 + 9x$')
    
    plt.fill_between(x_arr, y_arr, 0, where=(y_arr > 0), color='green', alpha=0.3, label='f(x) > 0')
    plt.fill_between(x_arr, y_arr, 0, where=(y_arr < 0), color='red', alpha=0.3, label='f(x) < 0')
    
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Закрашенные области, где f(x) > 0 и f(x) < 0')
    plt.legend(loc='best')
    plt.grid(True, alpha=0.3)
    
    plt.show()

def chart_8():
    """
    Сравнивает сходимость двух методов с аппроксимацией в логарифмическом масштабе
    """
    N = np.array([10, 100, 1000, 10000, 100000])
    error_A = np.array([0.1, 0.03, 0.01, 0.003, 0.001])
    error_B = np.array([0.1, 0.05, 0.025, 0.012, 0.006])

    plt.figure(figsize=(10, 6))
    plt.loglog(N, error_A, 'o-', linewidth=2, markersize=6, label='Error A')
    plt.loglog(N, error_B, 'o-', linewidth=2, markersize=6, label='Error B')

    log_N = np.log(N)
    log_error_A = np.log(error_A)
    log_error_B = np.log(error_B)
    
    c_A = np.polyfit(log_N, log_error_A, 1)
    c_B = np.polyfit(log_N, log_error_B, 1)
    
    p_A = np.poly1d(c_A)
    p_B = np.poly1d(c_B)
    
    t_A = np.exp(p_A(log_N))
    t_B = np.exp(p_B(log_N))
    
    plt.loglog(N, t_A, '--', alpha=0.7, label=f'Аппроксимация A')
    plt.loglog(N, t_B, '--', alpha=0.7, label=f'Аппроксимация B')
    
    plt.xlabel('N (количество точек)')
    plt.ylabel('Error (ошибка)')
    plt.title('Сравнение сходимости методов A и B')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.show()

def chart_9():
    """
    Создает гексагональную карту плотности для визуализации распределения точек
    """
    n = 5000
    
    x1 = np.random.normal(2,1, int(0.7 * n))
    y1 = np.random.normal(3,1, int(0.7 * n))

    x2 = np.random.normal(6, 1, int(0.3 * n))
    y2 = np.random.normal(7, 1, int(0.3 * n))

    x_arr = np.concatenate((x1, x2))
    y_arr = np.concatenate((y1, y2))

    hb = plt.hexbin(x_arr, y_arr, cmap='viridis')
    plt.colorbar(hb)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Гексагональная карта плотности точек")
    plt.show()

def chart_10():
    """
    Сравнивает распределения трех групп данных с помощью violin plot и box plot
    """
    A = np.random.normal(70, 10, 100)
    B = np.random.normal(75, 5, 100)
    C = np.random.uniform(50, 90, 100)

    ABC = [A,B,C]
    labels = ['Группа A', 'Группа B', 'Группа C']

    plt.violinplot(ABC)
    plt.xticks([1, 2, 3], labels)
    plt.xlabel("Группы")
    plt.ylabel("Оценки")
    plt.title("Сравнение распределений оценок")
    plt.grid(True)
    plt.show()

    plt.boxplot(ABC)
    plt.xlabel("Группы")
    plt.ylabel("Оценки")
    plt.title("Boxplot сравнение распределений оценок")
    plt.grid(True)
    plt.show()
    
def chart_11():
    """
    Анализирует сходимость алгоритма через аппроксимацию ошибки по итерациям
    """
    iterations = np.array(list(range(1, 21)))
    errors = np.array([1.0, 0.5, 0.3, 0.2, 0.15, 0.12, 0.1, 0.09, 0.08, 0.075,
                       0.07, 0.068, 0.065, 0.063, 0.061, 0.06, 0.059, 0.058, 0.057, 0.056])

    plt.figure(figsize=(10, 6))
    plt.plot(iterations, errors,'bo-', linewidth=2, markersize=6, label='Ошибка')

    log_iterations = np.log(iterations)
    log_errors = np.log(errors)
    
    c = np.polyfit(log_iterations, log_errors, 1)
    p = np.poly1d(c)
    
    t = np.exp(p(log_iterations))
    plt.plot(iterations, t, '--', alpha=0.7, label=f'Аппроксимация (наклон: {c[0]:.3})')
    
    plt.xlabel('Итерация')
    plt.ylabel('Ошибка')
    plt.title('График ошибки vs итерация')
    plt.legend()
    plt.grid(True)
    plt.show()

def chart_12():
    """
    Создает столбчатую диаграмму с отображением погрешностей измерений
    """
    methods = ['Метод A', 'Метод B', 'Метод C', 'Метод D']
    accuracy = [0.85, 0.88, 0.82, 0.91]
    error_bars = [0.03, 0.02, 0.04, 0.02]
    
    index = np.arange(len(methods))
    
    plt.figure(figsize=(10, 6))
    plt.bar(index, accuracy, yerr=error_bars, 
             error_kw={'ecolor':'0.1', 'capsize':6}, 
             alpha=0.7, label='Точность ± ошибка')
    
    plt.xticks(index, methods)
    plt.xlabel('Методы')
    plt.ylabel('Точность')
    plt.title('Сравнение методов с учетом неопределенности')
    plt.legend(loc='best')
    plt.grid(True, alpha=0.3)
    
    plt.savefig('bar_with_error_4.png', dpi=300, bbox_inches='tight')
    plt.show()

def chart_13():
    """
    Изображает график с двумя осями X
    """
    x_arr = np.linspace(-1,5,500)
    y1_arr = function_2_1(x_arr)
    y2_arr = function_2_2(x_arr)
    
    fig, ax = plt.subplots(figsize=(10, 5))

    line1 = ax.plot(x_arr, y1_arr,color='red', label='Функция 1')
    ax.set_xlabel('X',color='black')
    ax.set_ylabel('Y1', color='blue')

    ax2 = ax.twiny()
    line2 = ax2.plot(x_arr, y2_arr, label='Функция 2')
    ax2.set_xlabel('X2', color='red')

    plt.title('График с двумя осями X')
    plt.grid(True)
    plt.show()
    

def update(frame, line, x):
    """
    Функция обновления для анимации
    Args:
        frame (float): Текущий кадр анимации
        line (Line2D): Объект линии для обновления
        x (ndarray): Массив координат x
    Returns:
        line (list): Список обновленных объектов для анимации
    """
    line.set_ydata(np.sin(x * N + frame))
    return [line]

N = 13

def chart_14():
    """
    Создает анимированный график и сохраняет её в GIF файл
    """
    x = np.linspace(0, 4*np.pi, 200)
    phasa = np.linspace(0, 4*np.pi, 100)

    fig, ax = plt.subplots()
    ax.set_xlim(0, 4*np.pi)
    ax.set_ylim(-1.5, 1.5)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title(f'Анимация волны: y = sin(x * {N} + t)')
    ax.grid(True)
    line, = ax.plot(x, np.sin(x * N))

    animation = FuncAnimation(
        fig,
        func=update,
        frames=phasa,
        fargs=(line, x),
        interval=40,
        blit=True,
        repeat=True
    )
    
    animation.save('wave.gif')
    plt.show()

def chart_15_or():
    """
    Изображает обчный график функции
    
    """
    x_arr = np.linspace(-1,5,500)
    y_arr = function_1(x_arr)
    
    plt.plot(x_arr, y_arr, linewidth=1)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(r'График функции: x^3 - 6x^2 + 9x')
    plt.grid(True)
    plt.savefig('function_plot_b.pdf')
    plt.savefig('function_plot_b.png')
    plt.show()
    
def chart_15():
    """
    Изображает публикационный график функции
    """
    x_arr = np.linspace(-1, 5, 500)
    y_arr = function_1(x_arr)

    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.size'] = 14
    plt.rcParams['lines.linewidth'] = 2
    
    plt.figure(figsize=(10, 6), dpi=300) 
    
    plt.plot(x_arr, y_arr, 'b-', label='$x^3 - 6x^2 + 9x$')
    
    plt.xlabel('Координата X')
    plt.ylabel('Координата Y')
    plt.title('График функции: $x^3 - 6x^2 + 9x$')
    plt.legend()
    plt.grid(True)
    
    plt.savefig('function_plot.pdf', dpi=300)
    plt.savefig('function_plot.png', dpi=300)
    plt.show()

if __name__ == "__main__":
    chart_1()
    chart_2()
    chart_3()
    chart_4()
    chart_5()
    chart_6()
    chart_7()
    chart_8()
    chart_9()
    chart_10()
    chart_11()
    chart_12()
    chart_13()
    chart_14()
    chart_15_or()
    chart_15()
