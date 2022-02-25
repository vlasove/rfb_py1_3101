# Методы словарей
words = {"one" : "один" , "two" : "два", "three" : "три", "four" : "четыре"}

my_personal_key = "one"

if my_personal_key in words: # words.keys()
    print(f"Key: {my_personal_key} Val:{words[my_personal_key]}")
else:
    print(None)

# Метод .get()
value = words.get("one")
print(".get():", value)

# Метод .get() с значением по умолчанию
birthdays = {"jan" : 0, "feb" : 5, "mar" : 3}
month = "dec"
print(birthdays.get(month, 0))

# val = birthdays["dec"] if "dec" in birthdays.keys() else 0

# Удаление пар из словаря
words = {"one" : "один" , "two" : "два", "three" : "три", "four" : "четыре"}
del words["two"]
print(words)

val = words.pop("one")
print(words)
print("Deleted one:", val)