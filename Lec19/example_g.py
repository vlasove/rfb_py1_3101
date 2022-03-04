"""
Запись нескольких строк в файл
"""

messages = ["Hello", "World", "!"]
fh = open(file="output.txt", mode="a")
fh.writelines([message + "\n" for message in messages]) # ["Hello\n", "World\n", "!\n"]
fh.close()