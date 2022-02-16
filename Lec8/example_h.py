# Решение задачи N
numerics = []

for _ in range(int(input())):
    numerics.append(int(input()))

print(sum(numerics[int(input())-1:int(input())]))
