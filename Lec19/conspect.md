## Лекция 19. Работа с файлами

* Начнем рассмотрение принципов работы с файлами на примере файлов `.txt`

### 1. Чтение файла целиком
* Сначала нужно создать файл-дескриптор (в нем будет содержаться вся неоходимая нам информация) : `open("path_to_file", "mode")
```py
fh = open(file="input.txt", mode="r")
print(fh)
fh.close()
```

* При создании дескриптора СОДЕРЖИМОЕ ФАЙЛА НЕ ЗАГРУЖАЕТСЯ В ПАМЯТЬ!

* То же самое только с помощью менеджера контекста `with`
```py
with open(file="input.txt", mode="r") as fh:
    content = fh.read()
    print("Content:", content)
```

### 2. Чтение файла построчно
* Построчное считывание через прямое создание дескриптора и его закрытие
```py
fh = open(file="input.txt", mode="r")

line = fh.readline()
line_num = 1
while line != "":
    print(f"Num:{line_num}, Content: {line.strip()}")
    line_num += 1
    line = fh.readline()


fh.close()
```
* Аналогично с менеджером контекста
```py
with open(file="input.txt", mode="r") as fh:
    line = fh.readline()
    line_num = 1
    while line != "":
        print(f"Num:{line_num}, Content: {line.strip()}")
        line_num += 1
        line = fh.readline()
```

* Считывание всех строк в виде списка
```py
fh = open(file="input.txt", mode="r")
lines = fh.readlines()
for line in lines:
    print(line.strip())
fh.close()
```

### 3. Перезапись файла
* Запись строки в файл:
```py
message = "Hello World!"
fh = open(file="output.txt", mode="w")
fh.write(message)
fh.close()
```

* Запись списка строк
```py
messages = ["Hello", "World", "!"]
fh = open(file="output.txt", mode="w")
fh.writelines([message + "\n" for message in messages])
fh.close()
```

### 4. Дозапись в файл
* Дозапись строки в файл:
```py
message = "Hello World!"
fh = open(file="output.txt", mode="a")
fh.write(message)
fh.close()
```

* Дозапись списка строк
```py
messages = ["Hello", "World", "!"]
fh = open(file="output.txt", mode="a")
fh.writelines([message + "\n" for message in messages])
fh.close()
```