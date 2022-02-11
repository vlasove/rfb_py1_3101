# Цикл for (range based for)
# for expression:
#      body

for i in range(1, 11, 1): # range(start, stop, step)
    print(i)

# Ограничение 1 : start,stop,step - исключительно целые числа!
# start: - с какого значения начать строить диапазон
# stop: до какого значения (не включая его), строить диапазон
# step: шаг, с каким будет построен диапазон

# По умолчанию step = 1
for i in range(1,5):
    print(f"{i} with step by default")

# Пол умолчанию start = 0
for i in range(7):
    print(f"{i} with start and step by default")

# Итерирование в обратную строку
board = 1
for i in range(10, -board, -1):
    print(f"{i} with negative step value")


# Когда вычисляется range?
numeric = 10
for i in range(1, numeric, 2):
    print(f"{i} with numeric stop")
    numeric += 2
    if numeric % 2 == 0:
        print("Numeric is even")