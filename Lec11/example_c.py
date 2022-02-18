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
x, y, z = 1, "Bob", True
print("X:", x, "Y:", y, "Z:", z)