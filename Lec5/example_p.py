# Решение задачи M
n = int(input())

for elem in range(-n, n+1):
    squared = elem ** 2
    print(f"Квадрат числа {elem} равен {squared}")