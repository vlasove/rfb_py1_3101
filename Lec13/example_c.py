# Функция с аргументами (простейшие)
def add(a, b):
    res = a**2 - b**2 - 3*a*b
    print("Result:", res)

add(1, 20) # С необходимо-позициональными аргументами (Required Positional Arguments)
add(20, 1)
add(a=10, b=50)
add(b=50, a=10)
add(a=-10, b=-25.5)
