# Логический тип bool
a_bool = True
b_bool = False


# Логические операции
print("a_bool AND b_bool:", a_bool and b_bool)
print("a_bool OR b_bool:", a_bool or b_bool)
print("not a_bool:", not a_bool)


# Арифметика с логическим типом
# Неявное преобразование в int -> 1 или 0
print(True * 2 + False ** True)