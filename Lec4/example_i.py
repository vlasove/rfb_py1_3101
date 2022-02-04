# Решение задачи A
a_float, b_float = float(input()), float(input())
sign = input()

if sign == "+":
    print(a_float + b_float)
elif sign == "-":
    print(a_float - b_float)
elif sign == "*":
    print(a_float * b_float)
elif sign == "/" and b_float != 0:
    print(a_float / b_float)
else:
    print("СБОЙ")