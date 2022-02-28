"""
Примеры использования функций
1) функции с одинаковыми именами переопределяют друг друга
    Означает, что последняя определенная функция является актуальной
"""

def add(a, b):
    """
    description
    """
    return a + b

def add(a, b ,c=100500):
    """
    description
    """
    return a + b + c 

def main():
    """
    entry point
    """
    print(add(2,3))

main()
