## Лекция 18. PIP и сторонние пакеты

* **PIP** - менеджер установки пакетов в `Python` (`pypi.org` - хранилище всех пакетов среди разработчиков `Python`)

* Для того, чтобы устанавливать пакеты через `pip`:
    1. Проверить, что `pip` установлен : `pip --version`
    2. Для установки `pip install <package_name>`

### 0. Настройка pip через proxy

1) Через proxy:

```
pip install --proxy http://username:password@proxy:port <package_name>
или
pip install --proxy https://username:password@proxy:port <package_name>
```

2) Или в командной строке можно задать:
```
set HTTP_PROXY=http://username:password@proxy:port
set HTTPS_PROXY=https://username:password@proxy:port
и выполняете
pip install <package_name>
```
* Пример:
```
pip --trusted-host pypi.python.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org install --proxy http://user:pass@proxy:port pandas
```


### 1. Забор пакетов из внутреннего хранилища
* `JFrog` - хранилище `python` пакетов (локальное), откуда также можно брать пакеты как общие , так и кастомные. (Инстуркция по работе с `JFrog` находилась на `Confluence`).
* Инструкция : https://confluence.raiffeisen.ru/pages/viewpage.action?pageId=221850837

### 2. Доп. команды
* `pip freeze` - показывает все установленные через `pip` в систему пакеты и библиотеки
* `pip uninstall <package_name>` - удалить выбранный пакет

### 3. Установка утилит для форматироввания
* Рассмотрим следующий код:
```py
def add(a,b):
                    return a +                b

def sub(c, c1):



 return c + c1


def mult(x,y         ):
    return                         x                        *                     y


def деление(o, o2):
 return o // o2


def main():
    a,b = int(input().strip()), int(input().strip())
    result = add(a,b) + add(b,a) + sub(add(a,a), mult(b,b)) - деление(b,a) ** 2 + add(a,b) + add(b,a) + sub(add(a,a), mult(b,b)) - деление(b,a) ** 2
    print(result)

if __name__ == '__main__':
    main() 
```

* Это рабочий код
* Какие проблемы есть в этом коде?
    * Отсутвие форматирования кода
    * Неудачные имена переменных 
    * Отсутствие документирования явных функций
    * Отстутствие однозначности явных функция (например add())

* В мире `Python` разработки существуют стандарты по написанию кода, регламентируются они общим `PEP8` : https://www.python.org/dev/peps/pep-0008/

* **Проблема 1** - форматирование
    * Решается проблема через утилиту `black` : `pip install black`
    * `black` - утилита для автоформатирования кода по стандарту `pep8`
    * Запуск `black module.py` или `python -m black module.py`
    * Существует еще стандартный форматер `autopep8` (по умолчанию установлен в `PyCharm`) - он неадекватный

* **Проблема 2** - неудачные имена
    * Решается проблема через утилиту `pylint` : `pip install pylint`
    * `pylint` - утилита-линтер (СЕМАНТИЧЕСКИЙ АНАЛИЗАТОР) - подсказывает, где выбраны неудачные имена, отсутствуют описания, представлены "кривые блоки" (излишние) кода, неиспользуемые переменные и т.д.
    * `pylint module.py` или `python -m pylint module.py`

* **Проблема 3** - остутсвуют правильно отформатированные строки документации
    * Решается проблема через утилиту `docformatter` : `pip install docformatter`
    * `docformatter` - утилита автоформатирования исключительно строк документации 
    * `docformatter -i module.py` или `python -m docformatter -i module.py`

* **Проблема 4** - если в коде есть зависимости, на их перечисление тоже есть стандарт
    * Решается проблема через утилиту `isort` : `pip install isort`
    * `isort` - утилита для сортировки и группировки зависимостей в пределах модуля по стандарту `pep8`
    * `isort module.py` или `python -m isort module.py`

* **Проблема 5** - остутствие статической типизации в языке
    * Эта проблема не решается
    * Но можно основываясь на аннотациях и итоговых вызовах функций в коде определить, где тип передаваемого аргумента не соответствует аннотируемому параметру функции!
    * Это решается через утилиту `mypy` : `pip install mypy`
    * `mypy` - утилита-чекер для проверки соответствия формального вызова функции с параметрами на совпадение с типами аннотируемых аргументов
    * `mypy module.py` или `python -m mypy module.py`
