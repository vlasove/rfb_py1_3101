# Простейший валидатор паролей
# Пользователь вводит пару паролей, валидатор их проверяет
# Пароли валидны, если длина больше 10 и пароли между собой совпадают
# В противном случае пользователь будет вводить пару паролей заново


while True:
    first_password = input()
    second_password = input()

    if len(first_password) <= 10:
        print("Слишком короткий пароль. Попробуй заново")
    elif first_password != second_password:
        print("Пароли различаются. Попробуй заново")
    else:
        print("НУ НАКОНЕЦ-ТО ПРАВИЛЬНО!")
        break