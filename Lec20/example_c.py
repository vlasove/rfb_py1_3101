# Пример записи в JSON. Ч.2. Запись в файл
import json

DATA = {
    "name" : "Bob",
    "last_name" : "Petrov",
    "link" : "https://facebook.com/accounts/?user=14213413"
}

GENERAL_DATA = {
    "first" : DATA,
    "second": DATA,
}


with open("data.json", "w") as fh:
    json.dump(obj=GENERAL_DATA, fp=fh, indent=4)
