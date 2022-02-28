"""
пример игнорирования default value arg
"""

def add(x_arg:int = 1, y_arg :int = 2, z_arg :int =3):
    """
    description
    """
    return x_arg + y_arg + z_arg

def main():
    """
    entry point
    """
    print(add(x_arg=5, z_arg=5))

main()