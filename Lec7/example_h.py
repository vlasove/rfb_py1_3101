# Неизменяемость строк
message = "Qello world!"
#message[0] = "H"
message = "H" + message[1:]
print(message)