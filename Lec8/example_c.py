# Индексация
nums = [10, 20, 30, 40, 50]
print("First elem:", nums[0])
print("Second elem:", nums[1])
print("Last elem:", nums[-1])

# Итерирование по индексу
for i in range(len(nums)):
    print(f"Id:{i} Elem:{nums[i]}")

# Конкатенация работает на любой индексируемой коллекции
zeros = [0] * 10
print(zeros)
ones = [1]
twos = [2,2,2]
print(ones + twos)