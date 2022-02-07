# Решение задачи I

SUCCESS_MSG = "Ну наконец-то!"
SHORT_PASSWORD_MSG = "Слишком короткий пароль!"
EASY_PASSWORD_MSG = "Слишком простой пароль!"
NOT_EQUAL_PASSWORDS_MSG = "Введенные пароли различаются!"


while True:
    first_password = input()
    second_password = input()

    if len(first_password) < 8:
        print(SHORT_PASSWORD_MSG)
    elif ("123" in first_password) or ("qwe" in first_password):
        print(EASY_PASSWORD_MSG)
    elif first_password != second_password:
        print(NOT_EQUAL_PASSWORDS_MSG)
    else:
        print(SUCCESS_MSG)
        break