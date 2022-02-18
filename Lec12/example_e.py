# Обработка словарей
words = {"one" : "один" , "two" : "два", "three" : "три", "four" : "четыре"}

# Количество пар (количество элементов) == количество ключей
print("Len:", len(words))

# Проверка вхождения
msg = "one"
if msg in words.keys(): # Есть ли msg в ключах словаря?
    print(f"{msg} in words")
    print(words.keys())

val = "один"
if val in words.values():
    print(f"{val} in words.values")
    print(words.values())

# Итерирование по ключам
for key in words.keys():
    print("Key:", key, "Value:", words[key])

# Итерирование по значениям
for val in words.values():
    print("Value:", val)


# Итерирование по парам
for key, value in words.items():
    print("Key:", key, "Value:", value)







