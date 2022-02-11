## Лекция 6. Коллекции. Множества.

В `Python` есть 5 стандартных коллекций:
* `set()` - множество
* `str()` - строка (как коллекция)
* `list()` - список
* `tuple()` - кортеж
* `dict()` - словарь


### 1. Множество. Определение и инициализация
* Множество - неупорядоченная (неиндексируемая) коллекция, способная хранить элементы любого типа, при этом уникализируя их.

* Инициализация пустого множества:
```
# Множества. Инициализация
numeric_set = set()

print("Set:", numeric_set)
print("Type:", type(numeric_set))
print("Length:", len(numeric_set))
```

* Иницализация с элементами:
```
# Множества. Инициализация
numeric_set = set([10,10, 10, 20, 20, 20, 30, 40, "Vasya", None, 22.5])
#numeric_set = {10,10, 10, 20, 20, 20, 30, 40, "Vasya", None, 22.5}


print("Set:", numeric_set)
print("Type:", type(numeric_set))
print("Length:", len(numeric_set))
```

* Пример вывода программы выше:
```
Set: {40, 10, None, 20, 'Vasya', 22.5, 30}
Type: <class 'set'>
Length: 7
```

* 1) Элементы встречаются по одному разу (дубликаты отбрасываются множеством)
* 2) Множество неупорядочено из-за отсуствия индексации и возможности хранить элементы рахного типа


* Наполнение множества элементами:
```
# Множество. Добавление элементов .add()
numeric_set = set()

numeric_set.add(10)
numeric_set.add(100500)
numeric_set.add(10)
numeric_set.add(-50)
numeric_set.add(-50)
numeric_set.add("Bob")
numeric_set.add(True)

print("Set:", numeric_set)
print("Len:", len(numeric_set))
```

* Простейшие операции над множествами:
```
# Операции над множествами (простейшие)

numeric_set = set([10, 20, 30, 40, 50,60])
# .add() - добавление элемента
numeric_set.add(-200)

# .pop() - удаление случайного элемента, если множество пустое - ошибка
elem = numeric_set.pop() 
print("Deleted elem:", elem)

# .remove(elem) - удаляет elem из множества, если elem нет во множестве - ошибка
numeric_set.remove(50)
print("Current set:", numeric_set)

# Проверка вхождения элемента во множество
if 50 in numeric_set:
    print("50 in numeric_set")
else:
    print("50 not in numeric_set")

# Пустое/не пустое
if len(numeric_set) == 0:
    print("set is empty")
else:
    print("set is not empty")
```


* Математические операции
```
# Математические операции
a_set = set([1,2,3,4])
b_set = set([3,4, 5,6])

# Пересечение - общие элементы двух множеств
c_set = a_set.intersection(b_set)
print("Intersection result:", c_set)


# Объединение - объединить элементы множеств в одно множество
d_set = a_set.union(b_set)
print("Union:", d_set)


# Вычитание (разность множеств) - элементы множества А, которыъ нет в множестве B
e_set = a_set.difference(b_set)
print("A - B:", e_set)
print("B - A:", b_set.difference(a_set))


# Симметрическая разность - объединение без пересечения
f_set = a_set.symmetric_difference(b_set)
print("A ^ B:", f_set)
```

* Обработка множеств
```
# Обработка множеств
numeric_set = set([10, 20, 30, 22.5, 12, 45, 32.5, -10])
total_sum = sum(numeric_set) # Если множество ТОЛЬКО из числовых типов (или приводимых к ним)
print("Sum:", total_sum)

min_num = min(numeric_set) # Если множество состоит только ИЗ СРАВНИМЫХ МЕЖДУ СОБОЙ элементов
print("Min:", min_num)

max_num = max(numeric_set)
print("Max:", max_num)

# Перебор элементов множества при помощи for
numeric_set.add(-10000000)
for elem in numeric_set: # Цикл for each
    print("Elem:", elem)
```
