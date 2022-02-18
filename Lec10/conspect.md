## Лекция 10. Коллекции. Списки. Продолжение

### 1. Списочные выражения. Пример
```
# Список из 100 нулей
zeros = [0] * 100
# print(zeros)

# Список из первых 100 натуральных чисел
numerics = []
for i in range(100):
    numerics.append(i)

#print(numerics)

# Список из первых 100 натуральных чисел, причем
# если число - четное - в список заносим квадрат числа
# в противном случае - куб
nums = []
for i in range(100):
    if i % 2 == 0:
        nums.append(i ** 2)
    else:
        nums.append(i ** 3)

print(nums)
```

* Без списочных выражений

```
"""
Общий синтаксис
lst = [elem for elem in iter]
"""

# Список из 100 нулей
zeros = [0 for _ in range(100)]
#print(zeros)

# Список из первых 100 натуральных чисел
numerics = [i for i in range(100)]
# print(numerics)

# Списочное выражение работает быстрее
# чем его аналог в виде цикла for с добавлением элементов

# a = val1 if expression else val2
nums = [i ** 2 if i % 2 ==0 else i ** 3 for i in range(100)]
print(nums)
```

* Те же самые задачи с использованием списочных выражений


### 2. Практические примеры использования списочных выражений
* Считывание с STDIN и преобразование на месте
```
nums = [int(str_elem) for str_elem in input().strip().split(sep=" ")]
print("Elems:", nums)
print("Sum:", sum(nums))
```

* Подготовить элементы к выводу в STDOUT
```
nums = [ 10, 20, 30, 40, 50, 60, 60]
print(" # ".join([str(elem) for elem in nums]))
```