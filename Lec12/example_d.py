# Какие могут быть ключи?
# Требование к ключам - неизменяемость!
words = {"one" : "один" , "two" : "два", "three" : "три"}
print(words["one"])
words["four"] = "четыре"
print("Len:", len(words))
print(words)

precisions = {0.5 : "плохая точность" , 0.8 : "достаточная точность" , 0.99: "высокая точность"}
print(precisions)
print(precisions[0.5])

sectors = {(0,0) : "начало координат", (10, 10) : "верхняя граница сетки координат"}
print(sectors)
print(sectors[(0,0)])

# Ключи можно смешивать (но не надо так делать)
bag = {10 : "a", 10.5:"b", True: "c", None : "d", "sting" : "e", (10, 10) : "f"}
print(bag)