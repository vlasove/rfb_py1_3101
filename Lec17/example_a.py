"""
Модуль, содержащий уберважные функции и объекты
"""

def add(x_arg:int, y_arg:int) -> int:
    """
    Сложение видов x^3 + y ^4
    """
    return x_arg ** 3 + y_arg ** 4


MAX_ATTEMPTS = 10

def main():
    for i in range(MAX_ATTEMPTS):
        print("Res:", add(i, i + MAX_ATTEMPTS))
        if i > 3 :
            break

if __name__ == '__main__':
    main()
    