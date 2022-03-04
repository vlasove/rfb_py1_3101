"""
Запись строки в файл
"""

message = "\n10000000"
fh = open(file="output.txt", mode="a") # mode="w" - перезапись, "а" - дозапись
fh.write(message)
fh.close()