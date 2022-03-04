# Пример записи в JSON. Ч.1. Сериализация и конвертация в строку
import json

DATA = {
    "name" : "Bob",
    "ids" : [1,2,3,4,5,6],
    "childs" : [
        {
            "name" : "Fedya",
            "age" : 10,
        }, 
        {
            "name" : "Natasha",
            "age" : 8,
        },
    ],
    "last_name" : "Petrov",
    "link" : "https://facebook.com/accounts/?user=14213413"
}


json_str = json.dumps(DATA, indent=4)
print(json_str)

new_dict = json.loads(json_str)
print(new_dict)

for child in new_dict["childs"]:
    print(child["age"])