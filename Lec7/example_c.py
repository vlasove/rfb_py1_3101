# Решение задачи I
first_word = input()

while True:
    current_word = input()
    if first_word[-1] == current_word[0]:
        first_word = current_word
        continue
    else:
        print(current_word)
        break
