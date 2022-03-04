"""
Построчное чтение из файла (с помощью контекстного менеджера)
"""

with open(file="input.txt", mode="r", encoding="cp1251") as fh:
    line = fh.readline()
    line_num = 1
    while line != "":
        print(f"Num:{line_num}, Content: {line.strip()}")
        line_num += 1
        line = fh.readline()

# Для бинарных файлов
# open(file="data.bin", mode="rb")