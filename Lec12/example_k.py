# Решение задачи D
birthdays = {}

n = int(input().strip())
for _ in range(n):
    friend_info = input().strip() # "Петя 12 фев"
    name, _, month = friend_info.split(sep=" ") # ["Петя" , "12", "фев"]
    if month not in birthdays.keys():
        birthdays[month] = [name] # "янв" : ["Федя"]
    else:
        birthdays[month].append(name) # "янв" : ["Федя" , "Коля"]
        birthdays[month].sort()

m = int(input().strip())
for _ in range(m):
    month = input().strip()
    names = birthdays.get(month, [])
    if len(names) == 0:
        print("")
    else:
        print(" ".join(names))