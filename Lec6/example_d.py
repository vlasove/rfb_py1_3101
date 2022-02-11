# Операции над множествами (простейшие)

numeric_set = set([10, 20, 30, 40, 50,60, "Alex"])
# .add() - добавление элемента
numeric_set.add(-200)
print("Set before deletion:", numeric_set)
# .pop() - удаление случайного элемента, если множество пустое - ошибка
elem = numeric_set.pop() 
print("Deleted elem:", elem)
print("Set after deletion:", numeric_set)

# .remove(elem) - удаляет elem из множества, если elem нет во множестве - ошибка
numeric_set.remove(50)
print("Current set:", numeric_set)

# Проверка вхождения элемента во множество
if 50 in numeric_set:
    print("50 in numeric_set")
else:
    print("50 not in numeric_set")

# Пустое/не пустое
if len(numeric_set) == 0:
    print("set is empty")
else:
    print("set is not empty")