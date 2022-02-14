# Строки. Индексация

message = "Hello World!"
print("First letter:", message[0])
print("First letter type:", type(message[0]))

print("Second letter:", message[1])

print("Last letter:", message[len(message) - 1])
print("Pre-last letter:", message[len(message) - 2])

# Синтаксический сахар "отрицательных индексов" (не нужно писать len(message))
print("Last letter:", message[-1]) # message[len(message) - 1]
print("Pre-last letter:", message[-2])

# Итерирование по индексам
for i in range(len(message)): #range(start=0, stop[, step=1)
    print(f"Letter {i} is {message[i]}")