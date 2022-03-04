# Исключения. Обработка исключений

def danger(n:int) -> float:
    """
    Возвращает результат 1/n
    """
    return 1 / n

def main():
    """
    Основная точка входа в приложение
    """
    try:
        arg = int(input())
        danger(arg)
    except ZeroDivisionError as z_err:
        print("Happend:", z_err)
        print("Danger should used non 0 aruments!")
    except TypeError as t_err:
        print("Happend:", t_err)
        print("Danger should used only int argument")
    except KeyboardInterrupt as k_err:
        print("Happend:", k_err)
        print("Don't press Ctrl+C")
    except ValueError as v_err:
        print("STDIN used to int read:", v_err)
    except:
        print("Another exception")
    else:
        print("Hooorayy!")
    finally:
        print("Hoorraayy2!!")

if __name__ == '__main__':
    main()