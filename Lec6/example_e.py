# Решение задачи R
IS_VALID = "ЗАСЧИТАНО"
IS_INVALID = "НЕ ЗАСЧИТАНО"

words = set()

for _ in range(int(input())):
    words.add(input())

if input() in words:
    print(IS_INVALID)
else:
    print(IS_VALID)

##############################################################################

# Решение задачи R
IS_VALID = "ЗАСЧИТАНО"
IS_INVALID = "НЕ ЗАСЧИТАНО"

words = set()
n_words = int(input())

for i in range(n_words):
    word = input()
    words.add(word)

new_word = input()

if new_word in words:
    print(IS_INVALID)
else:
    print(IS_VALID)