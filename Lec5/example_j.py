# Нахождение min/max
# Вводим натуральные числа не больше 1000

CURRENT_MAX = -1
CURRENT_MIN = 2000

while True:
    numeric = int(input())
    if numeric < 0:
        break

    if numeric > CURRENT_MAX:
        print(f"Old max: {CURRENT_MAX} numeric: {numeric}")
        CURRENT_MAX = numeric

    if numeric < CURRENT_MIN:
        print(f"Old min: {CURRENT_MIN} and numeric {numeric}")
        CURRENT_MIN = numeric

print("Current max:", CURRENT_MAX)
print("Current min:", CURRENT_MIN)
