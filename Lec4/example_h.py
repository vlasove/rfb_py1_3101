# Имитатор калькулятор CalcBOSS9000 v1.0
# Который принимает 2 целых числа
# Так же считывает знак арифметической операции : "+", "-", "*"
# Если арифметический знак , введенный пользователем, поддерживается калькулятором
# то необходимо вывести результат этой операции над числами
# В противном случае - вывести "НЕ ПОДДЕРЖИВАЕТСЯ"

a_int = int(input())
b_int = int(input())
sign = input() #"+", "-"

if sign == "+":
    print(a_int + b_int)
elif sign == "-":
    print(a_int - b_int)
elif sign == "*":
    print(a_int * b_int)
else:
    print("НЕ ПОДДЕРЖИВАЕТСЯ")