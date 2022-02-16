# Методы списков
numerics = [10, 20, 30, 40, 30, 30]
# print(dir(numerics))

# 1) Списки - ссылочный тип!
b = numerics[:] # numerics.copy()
b.append(9999999)
print("Numerics:", numerics)
print("b:", b)

# 2) .count() - подсчет количества вхождений
print("30 in in numerics:", numerics.count(30))

# 3) .extend() - подшивает другой список в конец исходного
numerics.extend([9999, 99,9999])
print(".extend():", numerics)

# 4) .index()
print(".index():", numerics.index(30))

# 5) .reverse()
numerics.reverse()
print(".reverse():", numerics)