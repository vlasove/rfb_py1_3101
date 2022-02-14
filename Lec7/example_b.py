# Решение задачи H
yes_set = set(["да", "Да", "дА", "ДА", "ад", "аД", "АД", "Ад"])
word = input() # "домА"

if (word[0] + word[-1]) in yes_set:
    print("СОГЛАСЕН")
else:
    print("НЕ СОГЛАСЕН")