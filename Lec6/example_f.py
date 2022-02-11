# Математические операции
a_set = set([1, 2, 3, 4])
b_set = set([3, 4, 5, 6])

# Пересечение - общие элементы двух множеств
c_set = a_set.intersection(b_set)
print("Intersection result:", c_set)


# Объединение - объединить элементы множеств в одно множество
d_set = a_set.union(b_set) # union_updated()
print("Union:", d_set)


# Вычитание (разность множеств) - элементы множества А, которыъ нет в множестве B
e_set = a_set.difference(b_set)
print("A - B:", e_set)
print("B - A:", b_set.difference(a_set))


# Симметрическая разность - объединение без пересечения
f_set = a_set.symmetric_difference(b_set)
print("A ^ B:", f_set)