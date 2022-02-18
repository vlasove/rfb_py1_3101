# На вход программа через STDIN поступает набор чисел (натуральных)
# разделенных пробелом
list_with_integers = [int(elem) for elem in input().strip().split(sep = " ")]

print("Elem:", list_with_integers)
print("Sum:", sum(list_with_integers))