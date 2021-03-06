# Встроенные обработчики коллекций
numerics = set([10, 20, 30, 40, 10, 20.5, -20, 20, 20, 20, 20,30, 40,60, 77, 60])
# Сумма всех элементов множества - только когда все элементы - числовые
total_sum = sum(numerics)
print(f"Total sum: {total_sum}")

# Поиск минимума/максимума в коллекции
# При использовании min/max нужно гарантировать, чтобы все элементы
# множества были сравнимы попарно!
print("Min:", min(numerics))
print("Max:", max(numerics))


# Перебор элементов множества
for elem in numerics:
    print(elem)

# Коллекции, которые можно использовать в цикле for для перебора элементов (итерирования)
# - называют ИТЕРАТОРАМИ