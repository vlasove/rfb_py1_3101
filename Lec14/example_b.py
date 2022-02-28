"""
Аргументы со значением по умолчанию (Default Values Args)
"""

def shift(shifting, x_arg = 0.0, y_arg = 0.0):
    """
    shifting - абсолютное значение сдвига (обязательный параметр)
    x_arg, y_arg - начальные координаты до сдвига (необязательные параметры, по умолчанию 0.0)

    возвращает кортеж (x_arg + shift, y_arg + shift)
    """
    return (x_arg + shifting, y_arg + shifting)

def main():
    """
    входная точка в приложение
    """
    x, y = shift(10, x_arg=5)
    print(f"X:{x}, Y:{y}")

main()