# Исключения. Обработка исключений

def danger(n:int) -> float:
    """
    Возвращает результат 1/n
    """
    return 1/ n


def main():
    """
    Основная точка входа в приложение
    """
    try:
        danger(0)
    except ZeroDivisionError as z_err:
        print("Happend:", z_err)
        print("Danger should used non 0 aruments!")

    print("Done!")

if __name__ == '__main__':
    main()