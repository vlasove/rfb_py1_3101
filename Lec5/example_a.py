# Решение задачи B
login = input()
email = input()

INCORRECT_LOGIN_MSG = "Некорректный логин"
INCORRECT_EMAIL_MSG = "Некорректная почта"
SUCCESS_MSG = "ОК"

if len(login) < 10 or "@" in login:
    print(INCORRECT_LOGIN_MSG)
elif not ("@" in email) or not ("." in email):
    print(INCORRECT_EMAIL_MSG)
else:
    print(SUCCESS_MSG)