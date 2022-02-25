# На вход программе поступает n - информация про друзей
# Про каждого друга известно "Имя Месяц" (где имя - имя друга, месяц - это месяц когда он родился)
# Задача - сохранить друзей удобным для обработки образом

# Через проверку добавленного ключа
birthdays = {}

n = int(input().strip())
for _ in range(n):
    friend_info = input().strip() # "Петя фев"
    name, month = friend_info.split(sep=" ") # ["Петя" , "фев"]
    if month not in birthdays.keys():
        birthdays[month] = [name] # "янв" : ["Федя"]
    else:
        birthdays[month].append(name) # "янв" : ["Федя" , "Коля"]

for month, names in birthdays.items():
    names_str = ', '.join(names)
    print(f"Month:{month} and birthdays at: {names_str}")