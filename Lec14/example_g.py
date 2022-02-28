"""
Функции с переменным количеством аргументов? О_о
Континуальные аругменты - обвзяки над коллекциями, которые позволяют принимать
неограниченное количетсво аргументов
*f    -
*temp - т.е. тут важно * в самом начале
*var  -
"""

def add(x_arg:int, y_arg:int, *args:int) -> int:
    """
    args -> tuple(obj1,obj2,obj3, ....)
    """
    print(f"X:{x_arg}, Y:{y_arg}")
    print("Tuple?:", type(args))
    print("Values?:", args)


def main() ->None:
    """
    entry point
    """
    add(1,2,3,4,5,6)
    add(1,2)
    add(2,3,4)
    add(1,4,4,3,3,2,4,6,5,3,2,4,5,5,3,2,2,2,5,5,4)

main()