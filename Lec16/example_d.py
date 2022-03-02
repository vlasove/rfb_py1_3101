"""
Анонимные функции, примеры
"""

numerics = [10, 20, 30, 40, 1, 2, 3, 4]

for i in range(len(numerics)):
    numerics[i] = (lambda value, id: value ** 2 + (id+100))(numerics[i], i)
    print(f"After {i}-th lambda call: ", numerics)
    print("=" * 20)