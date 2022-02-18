# Добавление новых элементов (новых пар)
transition = {10: "ten", 11: "eleven"}
transition[12] = "twelve" # Добавление как ключа, так и значения!
print(transition)

transition[10] = "TEN" # Перезапись значения по существующему ключу 10
print(transition)
print(transition[10]) # Чтение из словаря по ключу 10