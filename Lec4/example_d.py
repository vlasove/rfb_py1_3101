# Условный оператор с блоком else
# if exression:
#     body_if
# else:
#     body_else

password = input()

if len(password) > 10:
    print("Good password")
else:
    print("Too short password")

print("Done")