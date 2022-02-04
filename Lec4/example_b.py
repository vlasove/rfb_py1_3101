# Как составить и из чего составляют логические выражения?

# Логические выражения из чисел
a_int = 205 # тоже самое можно сделать с float/float, или float/int
b_int = 200

print("a > b", a_int > b_int)
print("a < b", a_int < b_int)
print("a >= b", a_int >= b_int)
print("a <= b", a_int <= b_int)
print("a == b", a_int == b_int)
print("a != b", a_int != b_int)

# Комбинация
print("a > b and a - четное число", a_int > b_int and a_int % 2 ==0)


# Логические выражения на строках
message = "Hello world!"
print("Длина сообщения > 10", len(message) > 10)
prefix = "hello" # "Hello"
print("Вхождение подстроки 'ello'", prefix in message)
# Проверка равенства строк с точностью до регистра
print("asd" == "asd") # True
print("asdf" != "asd") # True


# На логическом типе
print(True and False and not True)

