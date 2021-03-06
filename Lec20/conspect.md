# Лекция 21. Итоговое занятие

* Отладчик
* Принципы работы с файлами (`.json`, `.xlsx`)
* Исключения (обработка)

## 1. Отладчик
* **Отладка** - это процесс "построчного" (пошагового) выполнения кода с целью нахождения логических ошибок.

* В `python` существует встроенный отладчик (но он очень неудобный), поэтому будем пользоваться отладчиком графической среды, в которой пишем код. Для того, чтобы отладчик среды правильно кооперировался с интерпреттором/компилятор в ОС, необходимо:
    * 1. И интерпретатор и компилятор должны быть установлены таким образом, чтобы их местоположение было известно ОС на уровне переменных окружений (Python - ADD TO PATH, VSCODE - Add to Path)
    * 2. Нужно отконфигурировать среду, чтобы ей было известно хотя бы местоположение интерпретатора/компилятора. (VSCODE configs to debugger)

* Допусти имеется код следующего вида:
```
# Код с логической ошибкой
COUNT = 10
result = 0

for i in range(COUNT):
    result = i % 10 + i // 3 + 2 # +2 - ошибочное действие

print("Result:", result)
```

* Действие 1 - локализовать возможную область ошибки
* Действие 2 - простановка `breakpoints` на каждой строке кода в области ошибки
* Действие 3 - запускаем отладчик 
* Действие 4 - находим панель с значениями переменных
* Действие 5 - начинаем пошаговую проверку
* Действие 6 - исправляем ошибку и поворяем шаги 1-6 до тех пор, пока код не станет работать так, как нужно.


### 2. Работа с JSON
* `JSON` - Java Script Object Notation - это формат файлов, в котором данные представляются в виде объектов JS.

* Для работы с `json` необходимо:
    1. Модуль `impore json`
    2. Создать дескриптор через `open()` (можно только `w` и `r` режимы, дозаписи нет)
    3. Воспользоваться одной из четырех функций модуля `json` 
        * `dump` - превратить объект (`python`) в байтовую строку и поместить в файл `.json`
        * `dumps` - превратить объект (`python`) в байтовую строку и поместить ее в переменную
        * `load` - загрузить объект из `.json` (загрузится байтовая строка и превратится в объект python)
        * `loads` - загрузить объект из байтовой строки