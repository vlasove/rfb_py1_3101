## Лекция 7. Коллекции. Строки

**Строка** (str) - это упорядоченная (индексируемая) коллекция, способная хранить элементы ОДНОГО типа.

### 1. Индексация в строках.
```
# Строки. Индексация

message = "Hello World!"
print("First letter:", message[0])
print("First letter type:", type(message[0]))

print("Second letter:", message[1])


print("Last letter:", message[len(message) - 1])
print("Pre-last letter:", message[len(message) - 2])

# Синтаксический сахар "отрицательных индексов" (не нужно писать len(message))
print("Last letter:", message[-1])
print("Pre-last letter:", message[-2])

# Итерирование по индексам
for i in range(len(message)): #range(start=0, stop[, step=1)
    print(f"Letter {i} is {message[i]}")
```

### 2. Сравнение строк
```
# Сравнение строк
lhs_word = "abcd"
rhs_word = "abc"

print(lhs_word < rhs_word)
# ord(str) -> int, chr(int) -> str
# В Python все строки хранятся как unicode
# ASCII - сколько всего символов в стандарте
print("Code a is :", ord("a"))
print("Code is A:", ord("A"))
print("Code B is:", ord("B"))
print("Code Y is:", ord("Y"))

# for i in range(60, 150):
#     print(f"Character of {i}:", chr(i))

# Как сравниваются строки?
# "abcd"   <    "abc"
# 1)  ord("a")  ==   ord("a")
# 2)  ord("b")  ==   ord("b") 
# 3)  ord("c")  ==   ord("c")
# 4)  ord("d")  >>   А ТУТ НЕТ БУКВЫ :) -> False
```

### 3. Срезы (слайсы) строк
```
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

c_slice = message[8::3] # От 5 индекса до конца
# От 8 индекса до конца с шагом в 3
print(c_slice)

# Срез/слайс любой коллекции - это объект того же типа, что и коллекция
print(message[:-1:1])


# Синтаксический сахар для срезов - разворот строки
print(message[::-1])
```

* 1) Срез строки - это строка
* 2) При срезании строк создаются новые строки (т.е. исходная не меняется)


### 4. Методы строк (популярные)
```
# Методы строк
msg = "#######heLLo World 15316######"
#print(dir(msg))

# Измненение регистра строки
upper_msg = msg.upper()
print(".upper():", upper_msg)

lower_msg = msg.lower()
print(".lower():", lower_msg)

capitalize_msg = msg.capitalize()
print(".capitalize():", capitalize_msg)


# Узнать, на каком индексе стоит символ (первое вхождение)
if "W" in msg:
    print("index():", msg.index("W"))

# Узнать, сколько раз встрчечается та или иная подстрока
print(".count():", msg.count("LL"))

# strip()
print(".rstrip():", msg.rstrip("#"))
print(".lstrip():", msg.lstrip("#"))
print(".strip():", msg.strip("#"))


# .replace()
print(".replace():", msg.replace("#", "."))
```

* Ни один из методов строк не изменяет ее исходного состояния!