# Решение задачи N
n = int(input())
numerics = []

for _ in range(n):
    num = int(input())
    numerics.append(num)

a, b = int(input()), int(input())
total_sum = 0

for elem in numerics[a-1:b]:
    total_sum += elem

print(total_sum)