words = {"one" : "один" , "two" : "два", "three" : "три", "four" : "четыре"}

keys_list = []
for key in words.keys():
    keys_list.append(key)

keys_list.sort()

for k in keys_list:
    print("Key:", k, "Value:", words[k])