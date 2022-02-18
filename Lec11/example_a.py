message = "Hello World!"

for i in range(len(message)):
    print("Id:", i, "Letter:", message[i])

for letter in message[::-1]:
    print("Letter:", letter)