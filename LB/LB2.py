
class DataSet:
    def __init__(self, data: dict[str, float] = None):
        """
        Инициализация набора данных.
        
        Args:
            data (dict[str, float], optional): Начальные данные. Defaults to None.
        
        Raises:
            TypeError: Если data не является словарем.
        """
        if data is None:
            self.data = {}
        elif isinstance(data, dict):
            self.data = {}
            for key, value in data.items():
                if not isinstance(key, str):
                    raise TypeError("Все ключи должны быть str")
                if not isinstance(value, (int, float)):
                    raise TypeError("Все значения должны быть числами (int или float)")
                self.data[key] = float(value)
        else:
            raise TypeError("data должен быть dict")
        
    def add(self, key: str, value: float):
        """
        Добавление пары ключ-значение.
        
        Args:
            key (str): Ключ для добавления
            value (float): Значение для добавления
        
        Raises:
            TypeError: Если ключ не строка или значение не число
        """
        if not isinstance(key, str):
            raise TypeError("Ключ должен быть str")
        if not isinstance(value, (int, float)):
            raise TypeError("Значение должно быть числом (int или float)")
        self.data[key] = float(value)

    def remove(self, key: str):
        """
        Удаление пары по ключу.
        
        Args:
            key (str): Ключ для удаления
        
        Raises:
            KeyError: Если ключ не существует
            TypeError: Если ключ не строка
        """
        if not isinstance(key, str):
            raise TypeError("Ключ должен быть str")
        
        if key not in self.data:
            raise KeyError(f"Key '{key}' not found in dataset")
        
        del self.data[key]

    def keys(self):
        """Возвращает список всех ключей."""
        return list(self.data.keys())

    def values(self):
        """Возвращает список всех значений."""
        return list(self.data.values())
    
    def summary(self):
        """
        Возвращает статистическую сводку данных.
        
        Returns:
            dict: Словарь с ключами mean, min, max или None если данных нет
        """
        if not self.data:
            return {'mean': None, 'min': None, 'max': None}
        
        values = self.values()
        return {
            'mean': sum(values) / len(values),
            'min': min(values),
            'max': max(values)
        }

    def __contains__(self, key: str):
        """
        Проверка наличия ключа в наборе данных.
        
        Args:
            key (str): Ключ для проверки
        
        Returns:
            bool: True если ключ существует, иначе False
        """
        if not isinstance(key, str):
            raise TypeError("Ключ должен быть str")
        return key in self.data

    def __iter__(self):
        """Итерация по ключам набора данных."""
        return iter(self.data.keys())

    def __getitem__(self, key: str):
        """
        Получение значения по ключу.
        
        Args:
            key (str): Ключ для поиска
        
        Returns:
            float: Значение по ключу
        
        Raises:
            KeyError: Если ключ не существует
        """
        if not isinstance(key, str):
            raise TypeError("Ключ должен быть str")
        return self.data[key]

    def __setitem__(self, key: str, value: float):
        """
        Установка значения по ключу.
        
        Args:
            key (str): Ключ для установки
            value (float): Значение для установки
        
        Raises:
            TypeError: Если ключ не строка или значение не число
        """
        if not isinstance(key, str):
            raise TypeError("Ключ должен быть str")
        
        if not isinstance(value, (int, float)):
            raise TypeError("Значение должно быть числом (int или float)")
        
        self.data[key] = float(value)

    def __str__(self):
        """Строковое представление набора данных."""
        if not self.data:
            return "{}"
        
        result = "{"
        for key, value in self.data.items():
            result += f'"{key}": {value}, '
        return result.rstrip(", ") + "}"


if __name__ == '__main__':
    # Пример 1: Создание пустого набора данных
    print("=== Пример 1: Пустой набор данных ===")
    ds1 = DataSet()
    print(f"Пустой набор: {ds1}")
    print(f"Сводка: {ds1.summary()}")
    print()

    # Пример 2: Инициализация с данными
    print("=== Пример 2: Инициализация с данными ===")
    ds2 = DataSet({'temp': 25.5, 'pressure': 1013.25})
    print(f"Набор: {ds2}")
    print()

    # Пример 3: Добавление данных через add()
    print("=== Пример 3: Добавление данных ===")
    ds3 = DataSet()
    ds3.add('temperature', 23.7)
    ds3.add('humidity', 65.2)
    print(f"После добавления: {ds3}")
    print()

    # Пример 4: Добавление данных через __setitem__
    print("=== Пример 4: Добавление через индексацию ===")
    ds4 = DataSet()
    ds4['speed'] = 120.5
    ds4['distance'] = 45.3
    print(f"Через индексацию: {ds4}")
    print()

    # Пример 5: Получение значения по ключу
    print("=== Пример 5: Получение значения ===")
    ds5 = DataSet({'price': 99.99, 'quantity': 5.0})
    print(f"price = {ds5['price']}")
    print(f"quantity = {ds5['quantity']}")
    print()

    # Пример 6: Проверка наличия ключа
    print("=== Пример 6: Проверка наличия ключа ===")
    ds6 = DataSet({'a': 1.0, 'b': 2.0})
    print(f"'a' in ds6: {'a' in ds6}")
    print(f"'c' in ds6: {'c' in ds6}")
    print()

    # Пример 7: Итерация по ключам
    print("=== Пример 7: Итерация по ключам ===")
    ds7 = DataSet({'x': 10.0, 'y': 20.0, 'z': 30.0})
    print("Ключи:", end=" ")
    for key in ds7:
        print(key, end=" ")
    print("\n")

    # Пример 8: Удаление элемента
    print("=== Пример 8: Удаление элемента ===")
    ds8 = DataSet({'first': 1.1, 'second': 2.2, 'third': 3.3})
    print(f"До удаления: {ds8}")
    ds8.remove('second')
    print(f"После удаления: {ds8}")
    print()

    # Пример 9: Получение ключей и значений
    print("=== Пример 9: Ключи и значения ===")
    ds9 = DataSet({'alpha': 100.0, 'beta': 200.0})
    print(f"Ключи: {ds9.keys()}")
    print(f"Значения: {ds9.values()}")
    print()

    # Пример 10: Статистическая сводка
    print("=== Пример 10: Статистическая сводка ===")
    ds10 = DataSet({'test1': 85.0, 'test2': 92.0, 'test3': 78.0})
    stats = ds10.summary()
    print(f"Данные: {ds10}")
    print(f"Среднее: {stats['mean']:.2f}")
    print(f"Минимум: {stats['min']}")
    print(f"Максимум: {stats['max']}")
    print()

    # Пример 11: Обработка ошибок - неверный тип ключа
    print("=== Пример 11: Ошибка - неверный тип ключа ===")
    try:
        ds11 = DataSet()
        ds11.add(123, 45.6)  # Ключ не строка
    except TypeError as e:
        print(f"Ошибка: {e}")
    print()

    # Пример 12: Обработка ошибок - неверный тип значения
    print("=== Пример 12: Ошибка - неверный тип значения ===")
    try:
        ds12 = DataSet()
        ds12.add('valid_key', 'invalid_value')  # Значение не число
    except TypeError as e:
        print(f"Ошибка: {e}")
    print()

    # Пример 13: Обработка ошибок - удаление несуществующего ключа
    print("=== Пример 13: Ошибка - удаление несуществующего ключа ===")
    try:
        ds13 = DataSet({'existing': 1.0})
        ds13.remove('nonexistent')
    except KeyError as e:
        print(f"Ошибка: {e}")
    print()

    # Пример 14: Обновление существующего значения
    print("=== Пример 14: Обновление значения ===")
    ds14 = DataSet({'initial': 50.0})
    print(f"До обновления: {ds14}")
    ds14['initial'] = 75.0
    print(f"После обновления: {ds14}")
    print()

    # Пример 15: Цепочка операций
    print("=== Пример 15: Цепочка операций ===")
    ds15 = DataSet()
    ds15.add('step1', 10.0)
    ds15['step2'] = 20.0
    ds15.add('step3', 30.0)
    ds15.remove('step2')
    print(f"Результат: {ds15}")
    print(f"Сводка: {ds15.summary()}")
    print()

    # Пример 16: Работа с большими числами
    print("=== Пример 16: Большие числа ===")
    ds16 = DataSet()
    ds16['million'] = 1000000.0
    ds16['billion'] = 1000000000.0
    print(f"Данные: {ds16}")
    print(f"Сводка: {ds16.summary()}")
    print()

    # Пример 17: Работа с отрицательными числами
    print("=== Пример 17: Отрицательные числа ===")
    ds17 = DataSet({'below_zero': -15.0, 'above_zero': 25.0})
    print(f"Данные: {ds17}")
    print(f"Сводка: {ds17.summary()}")
    print()

    # Пример 18: Работа с дробными числами
    print("=== Пример 18: Дробные числа ===")
    ds18 = DataSet()
    ds18.add('pi', 3.14159)
    ds18.add('e', 2.71828)
    ds18.add('sqrt2', 1.41421)
    print(f"Данные: {ds18}")
    stats18 = ds18.summary()
    print(f"Среднее: {stats18['mean']:.5f}")
    print()

    # Пример 19: Комбинированные операции
    print("=== Пример 19: Комбинированные операции ===")
    ds19 = DataSet({'a': 10.0, 'b': 20.0})
    print(f"Исходные данные: {ds19}")
    
    # Добавляем новый элемент
    ds19.add('c', 30.0)
    print(f"После добавления 'c': {ds19}")
    
    # Обновляем существующий
    ds19['a'] = 15.0
    print(f"После обновления 'a': {ds19}")
    
    # Проверяем наличие ключей
    print(f"Есть ли 'b'? {'b' in ds19}")
    print(f"Есть ли 'd'? {'d' in ds19}")
    
    # Итерируемся
    print("Ключи в наборе:", list(ds19))
    print()

    # Пример 20: Граничный случай - один элемент
    print("=== Пример 20: Один элемент ===")
    ds20 = DataSet({'lonely': 42.0})
    stats20 = ds20.summary()
    print(f"Данные: {ds20}")
    print(f"Сводка: mean={stats20['mean']}, min={stats20['min']}, max={stats20['max']}")