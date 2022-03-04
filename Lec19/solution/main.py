"""Решение задачи B."""

from typing import Tuple

INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def get_coeffs_as_str_from_file(file_path: str):# -> str:
    """Возвращает строку с коэффициентами уравнения из файла file_path."""
    file_handler = open(file=file_path, mode="r")
    coeffs_str = file_handler.read().strip()
    file_handler.close()
    return coeffs_str


def get_numerics_coeffs_from_str(coeffs_str: str):# -> Tuple[float, ...]:
    """Преобразует числовую строку вида "a b c" в кортеж вида (a, b, c) и
    возвращает его."""
    return tuple([float(coeff) for coeff in coeffs_str.split(sep=" ")])


def write_result_to_file(file_path: str, result: int):# -> None:
    """Записывает result в файл file_path."""
    file_handler = open(file=file_path, mode="w")
    file_handler.write(str(result))
    file_handler.close()


def linear(coeff_b: float, _: float):# -> int:
    """
    Возвращает количество решений для уравнения
    вида Bx + C = 0
    * Если x существует - вернет 1, в противном случае - 0
    """
    if coeff_b == 0:
        return 0
    return 1


def quadratic(coeff_a: float, coeff_b: float, coeff_c: float):# -> int:
    """
    Возвращает количество решений для уравнения вида
    Ax^2 + Bx + C = 0, A != 0
    * Если дискриминант положителен - вернет 2
    * Если дискриминант нулевой - 1
    * В противном случае - 0
    """
    discrim = coeff_b ** 2 - 4 * coeff_a * coeff_c
    if discrim > 0:
        return 2
    if discrim == 0:
        return 1
    return 0


def solve(coeff_a: float, coeff_b: float, coeff_c: float):# -> int:
    """
    Функция для поиска общего решения уравнения
    вида Ax^2 + Bx + C = 0

    Возвращает количество корней данного уравнения
    """
    if coeff_a == 0:
        return linear(coeff_b, coeff_c)
    return quadratic(coeff_a, coeff_b, coeff_c)


def main():# -> None:
    """Основная точка входа в программу."""
    coeffs_str = get_coeffs_as_str_from_file(file_path=INPUT_FILE)
    coeff_a, coeff_b, coeff_c = get_numerics_coeffs_from_str(coeffs_str=coeffs_str)
    res = solve(coeff_a, coeff_b, coeff_c)
    write_result_to_file(file_path=OUTPUT_FILE, result=res)


if __name__ == "__main__":
    main()
