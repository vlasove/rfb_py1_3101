# Внешние счетчики
count = 0 # внешний счетчик четных чисел

while True:
    numeric = int(input())
    if numeric < 0 :
        break

    if numeric % 2 ==0:
        count += 1

print("Общее кол-во введенных четных чисел:", count)