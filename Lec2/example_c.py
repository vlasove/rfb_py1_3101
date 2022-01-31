# Форматирование строк и изменение стандартного поведения print()
name = "Bob"
last_name = "Johnson"
age = "22"

# Форматированные строки - f-strings
message = f"Hello! My name is '{name}', my lastname is !{last_name}!, age is {age}"
print(message)

# Еще один пример
word_a = "###"
word_b = "$$$"
word_c = "@@@"

new_message = f"{word_a}{word_b}{word_c}"
print(new_message)

# Изменение стандартных параметров print()
my_sep = "??"
my_end = "ENDLINE"
print(word_a, name, word_b, word_c, sep = my_sep, end = my_end)
print(last_name, age, sep = "****")