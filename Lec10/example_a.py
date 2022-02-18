# Список из 100 нулей
zeros = [0] * 100
# print(zeros)

# Список из первых 100 натуральных чисел
numerics = []
for i in range(100):
    numerics.append(i)

# print(numerics)

# # Список из первых 100 натуральных чисел, причем
# # если число - четное - в список заносим квадрат числа
# # в противном случае - куб
nums = []
for i in range(100):
    if i % 2 == 0:
        nums.append(i ** 2)
    else:
        nums.append(i ** 3)

print(nums)