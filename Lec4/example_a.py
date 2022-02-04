# Условный оператор
# Базовый синтаксис

# Однобокий условный оператор
# if expression:
#     body

# expression - логическое выражение (что после себя оставит True/False)
# body - тело условного опрератора (которое будет выполнено, в случае если expression ->True)

age = int(input())

if age > 18:
    print("You're 18+")
    print("Another line")
# Единое тело имеет единый отступ

print("Done")