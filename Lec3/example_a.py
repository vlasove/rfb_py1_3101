# Целые числа
a_int = int(input()) # int("10")
b_int = int(input()) # int("99")

print(f"A value {a_int} and B value {b_int}")
print("Type of A:", type(a_int))
print(a_int, b_int)
print("Values:", a_int, b_int)

# Арифметика
print("a_int + b_int = ", a_int + b_int)
print("a_int - b_int = ", a_int - b_int)
print("a_int * b_int = ", a_int * b_int)
# Нюанс при делении - всегда вещественное число!!!
print("a_int / b_int = ", a_int / b_int)
# Классическое целочисленное деление - это //
print("a_int // b_int = ", a_int // b_int)
# Взятие остатка от деления
print("a_int % b_int = ", a_int % b_int) # 5 и 3 -> |5 - (5//3)|
# Возведение в степень
print("a_int ^ b_int = ", a_int ** b_int)


Perimeter = 2 * (a + b) # a + a + b + b
Area = a * b 