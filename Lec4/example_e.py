# Пример. Вводится произвольная строка
# Если строка содержит символ "@" - вывести "Валидная строка"
# в противном случае - вывести "Невалидная строка"

email = input()

if "@" in email:
    print("Валидный email")
else:
    print("Невалидный email")