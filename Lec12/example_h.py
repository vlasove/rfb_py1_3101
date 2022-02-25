# Приложение с словарными карточками
# Хочу хранить карточки вида русское слово - английское слово
# Принимаем на вход n - количество карточек
# После этого идет информация об n карточках в виде: "рус англ"

# После этого хотим узнать информацию о 3 русских словах (т.е. введем 3 рус слова)
n = int(input().strip())
translation = {}

for _ in range(n):
    message = input().strip() # "собака dog"
    words = message.split(sep = " ") # ["собака" , "dog"]
    translation[words[0]] = words[1] # translation["собака"] = "dog"

for _ in range(3):
    print(translation.get(input().strip(), "НЕИЗВЕСТНЫЙ ПЕРЕВОД"))