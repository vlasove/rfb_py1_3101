# Методы строк
msg = "#######heLLo World 15316######"
# print(dir(msg))

# Измненение регистра строки
upper_msg = msg.upper()
print(".upper():", upper_msg)

lower_msg = msg.lower()
print(".lower():", lower_msg)

capitalize_msg = msg.capitalize()
print(".capitalize():", capitalize_msg)


# Узнать, на каком индексе стоит символ (первое вхождение)
if "W" in msg:
    print("index():", msg.index("W"))

# Узнать, сколько раз встрчечается та или иная подстрока
print(".count():", msg.count("LL"))

# strip()
print(".rstrip():", msg.rstrip("#"))
print(".lstrip():", msg.lstrip("#"))
print(".strip():", msg.strip("#"))


# .replace()
print(".replace():", msg.replace("#", "."))