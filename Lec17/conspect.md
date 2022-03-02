## Лекция 17. Модули и пакеты

* Модуль - это любой файл с расширением `.py`

## 1. Создание модуля для примера
```
def add(x_arg:int, y_arg:int) -> int:
    """
    Сложение вида x^3 + y ^4
    """
    return x_arg ** 3 + y_arg ** 4


MAX_ATTEMPTS = 10

for i in range(MAX_ATTEMPTS):
    print("Res:", add(i, i + MAX_ATTEMPTS))
    if i > 3 :
        break
```

## 2. Создадим сторонний модуль
* `example_b.py` и попробуем импортировать элементы из модуля `example_a.py`
```
import example_a

print(example_a.MAX_ATTEMPTS)
```

* При импортировании модуля - импортируемый модуль выполняется от начала до самого конца!
* При импортировании путь указывается в виде названия модуля (путь вида `C:/Users/.../` не используется).
* Принято, импортируемые модули держать в той же директории, где и находится основной модуль.

```
import example_of_super_functionality_a as example

print(example.MAX_ATTEMPTS)
print(example.add(10, 20))
```

* Выше приведен пример для задания местоименя на имя импортируемого модуля (теперь обращаться к модулю можно через `example`)

## 3. Разделяющая и совмещающая область видимости при импортировании
* Исходник
```
def add(x_arg:int, y_arg:int) -> int:
    """
    Сложение вида x^3 + y ^4
    """
    return x_arg ** 3 + y_arg ** 4


MAX_ATTEMPTS = 11
date = "2021-27-12"
```

* Импортирование:
```
import example_a as example


MAX_ATTEMPTS = "BOB"
date = "2020-11-11"

print(example.MAX_ATTEMPTS)
print(MAX_ATTEMPTS)

print("example_a:", example.date)
print("example_b:", date)
```

* В данном случае говорят, что модули импортируются на разделяющую области видимости. Это означает, что если в импортируемом и исходном модулях встречаются одинаковые имена - они друг друга не переопределят! Т.к. для обращения к имопртированному имени придется писать `<module_name>.<var_name>`. 

* Разделяющую область видимости используют в ситуациях, когда в разных модулях могут встречаться одинаковые имена (имена функций, имена переменных, даты, базы данных, коннекты и т.д.)

* Импортирование
```
from example_a import MAX_ATTEMPTS, date


MAX_ATTEMPTS = "BOB"
date = "2020-11-11"

print(MAX_ATTEMPTS)
print("example_b:", date)
```

* В данном случае происходит совмещение простанств имен модулей и теперь импортируя имена из модуля они включаются в текущий (т.е. могут быть переопределены).

* Используется для работы с уникальными именами (например `ApplicationName, ApplicationVersion, DataBaseConnectionString`) - т.е. на весь проект такая переменная должна быть одна.

### 4. __name__ == "__main__"
```
"""
Модуль содержащий набор элементов
для последующего взаимодействия с ними
через импортирование
"""

def add(x_arg:int, y_arg:int) -> int:
    """
    Сложение вида x^3 + y ^4
    """
    return x_arg ** 3 + y_arg ** 4


MAX_ATTEMPTS = 11
date = "2021-27-12"

def main() -> None:
    """
    """
    for i in range(MAX_ATTEMPTS):
        print("Res:", add(i, i + MAX_ATTEMPTS))
        if i > 3 :
            break

if __name__ == '__main__':
    main()
```

* Блок `if __name__ == '__main__'` используют для того, чтобы отделить импортируемую область модуля от неимпортируемой. (Помним, что в процессе импортирования разделюящего/совмещающего импортируемый модуль выполняется от начала до конца интерпретатором), но можно использовать синтаксическую конструкцию, которая позволит выполнять определенный код только в той ситуации, когда модуль был запущен напрямую через интерпретатор. Достигается это при помощи использования переменной `__name__`.
    * `__name__` == `__main__` только в тех случайх, когда модуль НАПРЯМУЮ вызвал интерпретатор (например в консоли написали `python example_a.py`)
    * `__name__` == `example_a` (в общем случае это путь импорта) в случае кода модуль импортируется (притягивается интерпретатором по цепочке импортов).


### 5. Пакеты
* Группа модулей (директория с модулями) - это пакет.
* При создании пакета важно помещать внутрь модуль с названием `__init__.py` (конструктор пакета), если его нет - старые версия питона думают, что это просто директория (для нее перестают работать пути импорта).