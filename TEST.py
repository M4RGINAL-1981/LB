import math

class Vector:
    """
    Класс Vector представляет математический вектор в n-мерном пространстве.
    
    Вектор - это объект, который имеет величину (длину) и направление. 
    В программировании вектор обычно представляется как набор чисел (компонентов),
    где каждое число соответствует координате в определенном измерении.
    
    В Python класс Vector является примером инкапсуляции математических операций
    над векторами в объектно-ориентированном стиле.
    """
    
    def __init__(self, components):
        self.components = components
    
    def __add__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Векторы должны иметь одинаковую размерность")
        
        result = [a + b for a, b in zip(self.components, other.components)]
        return Vector(result)
    
    def __sub__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Векторы должны иметь одинаковую размерность")
        
        result = [a - b for a, b in zip(self.components, other.components)]
        return Vector(result)
    
    def dot(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Векторы должны иметь одинаковую размерность")
        
        return sum(a * b for a, b in zip(self.components, other.components))
    
    def __mul__(self, scalar):
        result = [a * scalar for a in self.components]
        return Vector(result)
    
    def __rmul__(self, scalar):
        return self.__mul__(scalar)
    
    def magnitude(self):
        return math.sqrt(sum(a * a for a in self.components))
    
    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Невозможно нормализовать нулевой вектор")
        
        result = [a / mag for a in self.components]
        return Vector(result)
    
    def __str__(self):
        return f"Vector({self.components})"
    
    def __repr__(self):
        return f"Vector({self.components})"
    
    def dimension(self):
        return len(self.components)
    
    def __eq__(self, other):
        if not isinstance(other, Vector):
            return False
        return self.components == other.components


# Пример использования
if __name__ == "__main__":
    # Создание векторов
    v1 = Vector([1, 2, 3])
    v2 = Vector([4, 5, 6])
    
    # Сложение векторов
    v3 = v1 + v2
    print(f"Сумма векторов: {v3}")
    
    # Вычитание векторов
    v4 = v3 - v2
    print(f"Разность векторов: {v4}")
    
    # Скалярное произведение
    dot_product = v1.dot(v2)
    print(f"Скалярное произведение: {dot_product}")
    
    # Умножение на скаляр
    v5 = v1 * 2
    print(f"Умножение на скаляр: {v5}")
    
    # Правостороннее умножение
    v6 = 3 * v1
    print(f"Правостороннее умножение: {v6}")
    
    # Длина вектора
    magnitude = v1.magnitude()
    print(f"Длина вектора: {magnitude:.2f}")
    
    # Нормализация
    v7 = Vector([3, 4])
    v7_norm = v7.normalize()
    print(f"Нормализованный вектор: {v7_norm}")
    print(f"Длина нормализованного вектора: {v7_norm.magnitude():.2f}")
    
    # Размерность
    print(f"Размерность вектора: {v1.dimension()}")
    
    # Проверка равенства
    print(f"Векторы равны: {v1 == Vector([1, 2, 3])}")