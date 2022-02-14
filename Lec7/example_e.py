# Срезы строк


message = "Hello#world!"

new_message = message[0] + message[1] + message[2] + message[3] + message[4]
print("Message:", new_message)

slice_message = message[0:5:1] # str[start:stop[:step]
print("Slice message:", slice_message)


a_slice = message[0:5] # По умолчанию step = 1
print(a_slice)

b_slice = message[:5] # По умолчанию start = 0
print(b_slice)

c_slice = message[5:] # От 5 индекса до конца
print(c_slice)

# Только с другим шагом
b_slice = message[:8:2] # По умолчанию start = 0
# От начала до 8 индекса (не включая) с шагом в 2
print(b_slice)

c_slice = message[8::3] # От 8 индекса
# От 8 индекса до конца с шагом в 3
print(c_slice)

# Срез/слайс любой коллекции - это объект того же типа, что и коллекция
print(type(message[:-1:1]))


# Синтаксический сахар для срезов - разворот строки
print(message[::-1])


# Итерирование по элементам среза через индексы
example_slice = message[::-2]
for i in range(len(example_slice)):
    print(example_slice[i])


# Строка - это итератор!
for letter in message[::2]:
    print("Letter:", letter)