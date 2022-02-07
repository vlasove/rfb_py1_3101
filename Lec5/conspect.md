## Лекция 5. Циклы

В `Python` существует 2 конструкции циклов:
* `while` (`while-do`) - который позволяет запускаться в "условно-бесконечном режиме"
* `for` (`range based for`)

**Цикл** - локальный участок кода, который выполняется заранее известное количество раз(или до заранее известного события).

### 1. Синтаксис while
```
while expression:
    body
```

### 1.1 Простейший while True
* Для остановки итерирования цикла `while True` используем ключевое слово `break`
* `break` - при выполнении прерывает текущую итерацию (текущее выполнение тела цикла) и передает управление первой инструкции стоящей ЗА ПРЕДЕЛЕАМИ тела цикла.
```
# Условно-бесконечный while и первое ключевое слово break
while True:
    numeric = int(input())
    if numeric >= 100 and numeric % 2 ==0:
        print("It's over")
        break
    print("Current numeric:", numeric)

print("Out of while body")
```

* `continue` - при выполнении прерывает текущую итерацию (текущее выполнение тела цикла) и передает управление СЛЕДУЮЩЕЙ ИТЕРАЦИИ ЦИКЛА.
```
while True:
    numeric = int(input())
    if numeric >= 100 and numeric % 2 ==0:
        print("It's over")
        break
    if numeric % 9 == 0:
        print("Numeric % 9 and continue")
        continue
    print("Current numeric:", numeric)

print("Out of while body")
```

### 1.3 while для разных задачек
* while с внешним счетчиком
```
count = 0

while True:
    numeric = int(input())
    if numeric < 0:
        break

    if numeric % 2 ==0:
        count += 1

print("Count is:", count)
```

* while для подсчета неэффективного min/max
```
CURRENT_MAX = -1000000
CURRENT_MIN = 10 ** 10

while True:
    numeric = int(input())
    if numeric < 0:
        break

    if numeric > CURRENT_MAX:
        CURRENT_MAX = numeric

    if numeric < CURRENT_MIN:
        CURRENT_MIN = numeric

print("Current max:", CURRENT_MAX)
print("Current min:", CURRENT_MIN)
```

### 2. Синтаксис for
```
for expression:
    body
```

* Пример:
```
for i in range(0, 10, 1):
    print("Current i:", i)

```

* Генератор `range(start, stop, step)` - принимает только `int` (даже приводимые к `int` вещественные значения не являются корретными для `range()`)
