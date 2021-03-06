## Лекция 15. Документирование и аннотирование. Ч.1

* На `Pyhton` важно писать понятный и одозначный код.


### 1. Простейшее документирование
* В Python принятно оформлять документацию не в виду комментириев, а в виде специального вида строк `docstrings` (`"""документация"""`)
* Документировать необходимо - весь скрипт + каждую функцию (которая выполняет не самую очевидную логику)

### 2. Пример:
* До
```py
def factorial(n):
    res = 1
    if n <= 1:
        return res
    for i in range(2, n+1):
        res *= i
    return res


def main():
    n = int(input().strip())
    #if type(n) == int:
    for i in range(n+1):
        print(f"{i}! = {factorial(i)}")
    
main()
```

* После простейшего документирвоания
```py
"""
Модуль для решения задачи подсчета факторила,
содержит все необходимые функции для обработки I/O потоков и выполнения
арифметических расчетов
"""

def factorial(n):
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

print()

def main():
    """
    Основная точка входа в приложение. Обрабатывает I/O потоки
    и ..
    """
    n = int(input().strip())
    for i in range(n+1):
        print(f"{i}! = {factorial(i)}")
    factorial()
    
main()
```

### 3. Аннотирование
* Аннотирование - это указывание ЖЕЛАТЕЛЬНОГО типа переменной!
* Пример простейшего аннотирования:
```py
def add(a :int, b :int):
    """
    Многозначительная документация
    """
    return a + b
```
* Аннотированные аргументы ни в коем случае не ограничивают свои типы (не становятся статически типизированными), а лишь служат для того, чтобы показать пользователям функции, какой ЖЕЛАТЕЛЬНЫЙ тип аргументов вы готовы принять на вход этой функции.

* Аннотирвоание возвращаемого значения
```
def add(a :int, b :int) -> int:
    """
    Многозначительная документация
    """
    return a + b
```

* Чем можно аннотировать еще?

```
"""
Пример аннотаций
"""
from typing import List, Dict

def mutate(a:int, b:int, d : List[int]) -> List[int]:
    """
    Никто не знает как работает эта функция.
    Служит для примера аннотиций входных и выходных типов
    """
    return [a,b] + d

def build_map(key:str = "key", value:int=10) -> Dict[str, int] :
    """
    Строит словарь , где ключ - аргумент key
    а значение - аргумент value
    """
    return {key : value}

build_map()
```

* Аннотации никак не ограничвают функционал интерпретатора! (Не доабвляют `type-check` при передаче аргументов).
* Модуль с дополнительными аанотациями `typing` позволяет аннотировать коллекции и гибриды с сигнатурами вида `List[int], Dict[int, List[str]]` и т.д.
* Подробнее про аннотирование почитать тут: https://realpython.com/python-type-checking/
