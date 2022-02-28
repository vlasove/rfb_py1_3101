# Простейший возврат
def add(a, b):
    return a**2 + b**3

# add(2, -3)
# add(-3, 2)
# именованное обращение к аргументам (снимает требование к позициональности)
# add(b=20, a=10)
# Required Positional Args 
# add(1, 2, 3)
# add(10)

#########################
answer = add(2, -4) + add(1, 1) // 2 + add(2,3) ** 2
print(f"Answer:{answer}")
 