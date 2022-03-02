"""
Анонимные функции
"""

def add(x_arg:int, y_arg:int):
    """
    description
    """
    result = x_arg ** 2 + y_arg **3
    return result

# lambda x,y: x**2 + y**3
# 1. Нет блока def
# 2. Нет имени
# 3. Нельзя использовать аннотации (:type), lambda-expression после : сразу ждет тело
# 4. Тело lambda-expression - ЦЕЛОСТНАЯ ЕДИНАЯ КОМАНДА которая будет возвращена

def concat(lhs:str, rhs:str):
    return lhs + rhs

def main():
    """
    entry point
    """
    function_object = lambda x,y: x**2 + y**3
    concat_lambda = lambda x, y: x + y
    print("Type:", type(function_object))
    print("Value:", function_object)
    print("Result:", function_object(10, 20))
    print("-" * 15)
    print("Result Str:", concat_lambda("asd", "bcd"))
    print("-"*15)
    print("Type:", type(add))
    print("Value:", add)
    print("Result:", add(10, 20))

main()