# На вход программе поступает n - информация про друзей
# Про каждого друга известно "Имя Месяц" (где имя - имя друга, месяц - это месяц когда он родился)
# Задача - сохранить друзей удобным для обработки образом

# С прединициализированным словарем
birthdays = {
    "янв" : [],
    "фев" : [],
    "мар" : [],
    "апр" : [],
    "май" : [],
    "июн" : [],
    "июл" : [],
    "авг" : [],
    "сен" : [],
    "окт" : [],
    "ноя" : [],
    "дек" : [],
}

n = int(input().strip())
for _ in range(n):
    friend_info = input().strip() # "Петя фев"
    name, month = friend_info.split(sep=" ") # ["Петя", "фев"]
    # names_in_month = birthdays[month]
    # names_in_month.append(name)
    # birthdays[month] = names_in_month
    birthdays[month].append(name)
    # birthdays[month].append("....") -> [].append("...")

for month, names in birthdays.items():
    names_str = ', '.join(names)
    print(f"Month:{month} and birthdays at: {names_str}")