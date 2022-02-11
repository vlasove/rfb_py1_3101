# Подсчет суммы и произведения чисел
summ = 0
mult = 1

while True:
    num = int(input())
    if num <= 0 :
        break

    summ += num
    mult *= num

print("Сумма всех чисел:", summ)
print("Произведение всех чисел:", mult)