"""
Принятый стиль в Python
"""

def multiply(a, b):
    """
    Здесь будет документация multiply
    """
    return a * b
    
def main():
    """
    основная точка входа в приложение
    """
    first_arg = int(input())
    second_arg = int(input())

    result = multiply(first_arg, second_arg)

    print(result)

main()