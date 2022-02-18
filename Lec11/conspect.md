## Лекция 11. Коллекции. Кортежи

**Кортеж** (tuple) - упорядоченная (индексируемая) коллекция, способная хранить элементы любого типа, и гарантирующая НЕИЗМЕНЯЕМОСТЬ ХРАНИМЫХ ЗНАЧЕНИЙ.

### 1. Инициализация кортежа
* Пустой кортеж
```
# Инициализация кортежа
a_tuple = tuple()
b_tuple = ()

print("Len:", len(b_tuple))
print("Type:", type(a_tuple))
```
* С элементами
```
# С элементами
num_tuple = (10, 20, 30, 40, 50)
print("Len:", len(num_tuple))
print("Type:", type(num_tuple))
print("Value:", num_tuple)
```

### 2. Общие операции для индексируемых коллекций на прмиере кортежа
```
num_tuple = (10, 20, 30, 40, 50)

# Индексирование
print("0-th:", num_tuple[0])
print("Last:", num_tuple[-1])

# Срезы
print(num_tuple[::-1])
print(num_tuple[2:])


# Конкатенация
print(num_tuple * 3 + (10, 20))

# Проверка вхождения
if 30 in num_tuple:
    print("30 in num_tuple")

# Длина, сумма, мин/макс
print("Len:", len(num_tuple))
print("Sum:", sum(num_tuple))
print("Min/max:", min(num_tuple), max(num_tuple))

# Итерирование
for i in range(len(num_tuple)):
    print("Id:", i, "Elem:", num_tuple[i])

for elem in num_tuple:
    print("Elem:", elem)


# Распаковка кортежа (tuple unpack)
x, y, z = 1, 2, 3
print("X:", x, "Y:", y, "Z:", z)
```

### 3. Специфические операции с кортежами
```
Их нет)
```

### 4. Фокус
* Если кортеж хранит ссылочные типы - неизменяемость будет
касаться только хранимых ссылок (фактических значений ссылок), а не их содержимого

```
nums = (
    [1,2,3],
    [10, 20, 30],
)

print("0-th:", nums[0])
nums[0].append(4)
print(nums)
```