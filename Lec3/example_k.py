numeric = 10 # У этой переменной есть - тип, имя, значение, адрес
             # int, numeric, 10, xf00xf
print(numeric)
numeric = numeric + 1
             # int, numeric, 11, adfxo0sxf
             # SHADOWING - затенение (присваивание новой ссылки старому имени)
print(numeric)

name = "Bobby"
print(name)
name = name + " " + "Johnson"
print(name)