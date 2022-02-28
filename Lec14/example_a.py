"""
Что может пойти не так с RP args?
"""

def add(a, b, c = 4):
    return a + b + c


print(add(2, 3, 5)) # с = 5 изменяем
print(add(1, 2)) # чтобы тут по умолчанию c = 4
print(add(b=10, c =15, a= 22))