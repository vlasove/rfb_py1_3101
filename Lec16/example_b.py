"""
Пример объектности функций в Python
"""
from typing import Callable

def my_string_compare(lhs :str, rhs: str) -> bool:
    """
    lhs -...
    rhs - ...

    возвращает True, если len(lhs) > len(rhs) иначе, если длины равны
    возвращает lhs > rhs
    """
    print("а теперь вызывается функция my_string_compare")
    if len(lhs) == len(rhs):
        return lhs > rhs
    return len(lhs) > len(rhs)

def UID_compare(lhs :str, rhs :str, comparator:Callable) -> bool:
    """
    lhs - ....
    rhs - ....
    comparator - функция, сравнивающая 2 строки по правилу:
                                        1) если len(lhs) <> len(rhs) -> return ...
                                        2) если длины равны , то сравниваются лексикографически
    возвращает .....
    """
    print("это вызов функции UID_compare")
    return comparator(lhs, rhs)


def generater_adder() -> Callable:
    """
    """
    def add(a:int, b:int):
        """
        """
        return a + b
    return add

def main() -> None:
    """
    entry point
    """

    first_user_UID, second_user_UID = "Kdsjgvabjdlksfgh", "abc"
    print(UID_compare(lhs=first_user_UID, rhs=second_user_UID, comparator=my_string_compare))
    adder = generater_adder()
    print(adder(2,3))

main()