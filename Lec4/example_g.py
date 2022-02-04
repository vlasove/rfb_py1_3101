# Условный оператор множественного выбора

# if expression1:
#     body1
# elif expression2:
#     body2
# elif expression3:
#     body3
# .....
# else:
#     body_else

age = int(input())

if age <= 14:
    print("Учетная запись 'Родительская'")
    print("Another lint")
elif age > 21 and age <= 45:
    print("First 21 and 45")
elif age > 14 and age <= 21:
    print("Учетная запись с небольшими ограничениями на показ сервисов")
elif age > 21 and age <= 45:
    print("Учетная запись полная")
else:
    print("Учетная запись БЕЗ РЕКЛАМЫ")

print("Done")