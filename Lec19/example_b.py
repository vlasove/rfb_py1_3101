"""
Считывание файла целиком (при помощи контекстного менеджера with)
"""

with open(file="input.txt", mode="r") as fh:
    content = fh.read()
    print("Content:", content)