# Вещественные числа
a_float = float(input())
b_float = float(input())



print(f"A value {a_float} and B value {b_float}")
print("Type of A:", type(a_float))
print(a_float, b_float)

# Арифметика
print("a_float + b_float = ", a_float + b_float)
print("a_float - b_float = ", a_float - b_float)
print("a_float * b_float = ", a_float * b_float)
# # Нюанс при делении - всегда вещественное число!!!
print("a_float / b_float = ", a_float / b_float)
# Классическое целочисленное деление - это //
print("a_float // b_float = ", a_float // b_float)
# Взятие остатка от деления
print("a_float % b_float = ", a_float % b_float)
# Возведение в степень
print("a_float ^ b_float = ", a_float ** b_float)
# Ограничение количества десятичных цифр после запятой
x = 10.91827467328904876290487
print(f"{x:.2f}")