# Решение задачи D - НЕЗАКОНЧЕННОЕ РЕШЕНИЕ

x1_int = int(input())
y1_int = int(input())
x2_int = int(input())
y2_int = int(input())

if x2_int >= 1 and x2_int <= 8 and y2_int >= 1 and y2_int <= 8:
    if x2_int == x1_int + 1 and y2_int == y1_int + 2 or (x2_int == x1_int + 2 and y2_int == y1_int + 1):
        print("ДА")
else:
    print("НЕТ")