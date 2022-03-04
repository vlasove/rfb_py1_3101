"""Модуль содержащий пример того, как надо оформлять Python код."""


import os
from typing import AnyStr

import pandas


def add(x_arg: int, y_arg: int) -> int:
    """Арифметическое сложение аргументов."""
    return x_arg + y_arg


def sub(x_arg: int, y_arg: int) -> int:
    """Арифметическое вычитание аргументов."""
    return x_arg - y_arg


def mult(x_arg: int, y_arg: int) -> int:
    """Арифметическое умножение аргументов."""
    return x_arg * y_arg


def div(x_arg: int, y_arg: int) -> int:
    """Арифметическое деление аргументов."""
    return x_arg // y_arg


def main() -> None:
    """Основная точка входа в приложение."""
    first_arg, second_arg = int(input().strip()), int(input().strip())
    result = (
        add(first_arg, second_arg)
        + add(second_arg, first_arg)
        + sub(add(first_arg, first_arg), mult(second_arg, second_arg))
        - div(second_arg, first_arg) ** 2
        + add(first_arg, second_arg)
        + add(second_arg, first_arg)
        + sub(add(first_arg, first_arg), mult(second_arg, second_arg))
        - div(second_arg, first_arg) ** 2
    )
    print(result)


if __name__ == "__main__":
    main()
