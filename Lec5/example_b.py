# Решение задачи С
first_word = input()
second_word = input()
third_word = input()

SUCCESS_MSG = "ОК"
UNSUCCESSESS_MSG = "НЕ ПРАВИЛЬНО"

if first_word == "раз" and second_word == "два" and third_word == "три":
    print(SUCCESS_MSG)
elif first_word == "один" and second_word == "два" and third_word == "три":
    print(SUCCESS_MSG)
elif first_word == "1" and second_word == "2" and third_word == "3":
    print(SUCCESS_MSG)
else:
    print(UNSUCCESSESS_MSG)