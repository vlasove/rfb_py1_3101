# continue
# Подсчет суммы и произведения только четных чисел
summ = 0
mult = 1

while True:
    num = int(input())
    if num <= 0 :
        break
    
    if num % 2 != 0:
        print("Дальше считать бессмысленно, перехожу в начало цикла")
        continue # остановка текущей итерации и передача управления следующей итерации цикла
    
    summ += num
    mult *= num

print("Сумма всех чисел:", summ)
print("Произведение всех чисел:", mult)