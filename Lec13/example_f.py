"""
Более-менее полезная функция (docstring)
подсчет факториала n! = n * (n-1) * (n-2) * ... * 1
"""


def factorial(n):
    res = 1
    if n <= 1:
        return res

    for i in range(2, n+1):
        res *= i 
    return res

for i in range(1, 11):
    res = factorial(i)
    print(f"{i}! is equal to {res}")