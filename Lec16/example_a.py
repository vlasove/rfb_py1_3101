"""
Пример объектности функций
"""

def add(x_arg:int, y_arg:int):
    """
    description
    """
    return x_arg ** 2 + y_arg **2

def sub(x_arg:int, y_arg:int):
    """
    description
    """
    return x_arg**2 - y_arg**2

def main():
    """
    entry point
    """
    result = add # Присваивание функционального объекта в переменную
    print("Type?:", type(result))
    print("Value?:", result)
    print(result(10, 20))

    handlers = [add, sub] # Пример упаковки функциональных объектов в коллекции
    for handler in handlers:
        print(handler(2, 3))

main()