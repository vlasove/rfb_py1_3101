# Решение задачи K
message = input()
answer = ""

for letter in message[::2]:
    answer += letter * 3
print(answer)