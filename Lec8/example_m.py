# Удаление элементов

# Через метод .pop()
numerics = [ 10, 20, 30, 40, 50]
elem = numerics.pop(2) # Удаляет последний по умолчанию, если передан индекс- удалит по индексу
print("Elem deleted:", elem)
print("Numerics:", numerics)

# Через метод .remove() по значению (Первое слева-на-право)
if 50 in numerics:
    numerics.remove(50)
print("After .remove():", numerics)

# del
del numerics[0]
print("After del:", numerics)