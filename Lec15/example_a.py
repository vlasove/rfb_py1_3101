"""
Модуль содержит все необходимые функции для решения задачи
подсчета восхтительного и быстрого и супер эффективного факторила числа n!
"""

def factorial(n :int) -> int:
    """
    Функция подсчета факториала натурального числа n
    Args:
        * n : int - целое положительное число
    Result:
        * n! - факториал числа n
    Подробнее:
        Факториал подсчитывает по формуле .......
    """
    res = 1
    if n <= 1:
        return res
    for i in range(2, n+1):
        res *= i
    return res


def main() -> None:
    """
    entry point
    """
    n = int(input().strip())
    #if type(n) == int:
    for i in range(n+1):
        print(f"{i}! = {factorial(i)}")
    
main()