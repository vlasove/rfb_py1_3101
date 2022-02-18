# На вход программа через STDIN поступает набор чисел (натуральных)
# разделенных пробелом
line_with_numbers = input().strip() # "1 2 3 4 5 6 7 8 10"
list_with_strigs = line_with_numbers.split(sep = " ") # ["1", "2", "3", "4", "5", ... "10"]
list_with_integers = []

for str_elem in list_with_strigs:
    list_with_integers.append(int(str_elem))

print("Origin str:", line_with_numbers)
print("Origin list with strs:", list_with_strigs)
print("Elem:", list_with_integers)
print("Sum:", sum(list_with_integers))