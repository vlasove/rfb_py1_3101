# Решение задачи N
n = int(input())
# 5! = 5 * 4 * 3 * 2 * 1
# 4! = 4 * 3 * 2 * 1
# 6! = 6 * 5 * 4 * 3 * 2 * 1
result = 1
if n > 1:
    for i in range(2, n+1):
        result *= i

print(result)