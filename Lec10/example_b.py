"""
Общий синтаксис
lst = [elem for elem in iter]
"""
# Списик из значений от 0 до 99
numbers = [i for i in range(0, 100, 1)]
# print(numbers)

# Список из 100 нулей
zeros = [0 for _ in range(100)]
#print(zeros)

# Тернарный условный оператор
target = 101
value = 10 if target % 2 ==0 else 20
# print(value)
# if target % 2 == 0:
#     value = 10
# else:
#     value = 20


# Списочное выражение работает быстрее
# чем его аналог в виде цикла for с добавлением элементов

# a = val1 if expression else val2
nums = [i ** 2 if i % 2 ==0 else i ** 3 for i in range(100)]
print(nums)















