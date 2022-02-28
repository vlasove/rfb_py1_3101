"""
Порядок следования аргументов с default value
"""

def add(first_arg, second_arg, third_arg = 0):
    """
    first_arg - это ...
    second_arg - это другое ...
    third_arg - это совсем другое, это -...

    возвращает сумму вида first_arg + second_arg + third_arg
    """
    return first_arg + second_arg + third_arg


def main():
    """
    основная точка входа в приложение
    """
    print(add(1, 2, 3))
    print(add(10, 20))

main()