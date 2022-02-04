# Оптимизация (внутренняя) вычисления логических выражений

numeric = 10

if numeric > 12 and numeric / 0:
    print("Все хорошо")
else:
    print("Все плохо")

if numeric > 5 or numeric / 0:
    print("Все хорошо 2")
else:
    print("Все плохо 2")


# Synonimic casting to logical expression
age = 20
if age:
    print("Hello")

# Правила приведения к bool в expression (if, while)
# Любое число != 0 -> True
# Любое число == 0 -> False

# Любая строка (не пустая, len > 0) -> True
# Пустая строка (len ==0) -> False

# None -> False
# not None -> True

# САМАЯ БОЛЬШАЯ ГАДОСТЬ
num = None
if True:
    num = 20 # Переменные определенные в телах if/while/for АВТОМАТИЧЕСКИ ЗАНОСЯТСЯ В ГЛОБАЛЬНУЮ ОБЛАСТЬ ВИДИМОСТИ МОДУЛЯ!

print(num)