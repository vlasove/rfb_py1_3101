# Условно-бесконечный цикл while

while True:
    message = input()
    if message == "":
        break      # break - остановка текущей итерации и передача управления инструкции, стоящей ЗА ПРЕДЕЛЕАМИ ЦИКЛА
    print(message)
