# Решение задачи E
heigh_1 = int(input())
heigh_2 = int(input())
heigh_3 = int(input())

if heigh_1 >= heigh_2 and heigh_2 >= heigh_3:
    print(heigh_3)
    print(heigh_2)
    print(heigh_1)
elif heigh_1 >= heigh_3 and heigh_3 >= heigh_2:
    print(heigh_2)
    print(heigh_3)
    print(heigh_1)
elif heigh_2 >= heigh_1 and heigh_1 >= heigh_3:
    print(heigh_3)
    print(heigh_1)
    print(heigh_2)
elif heigh_2 >= heigh_3 and heigh_3 >= heigh_1:
    print(heigh_1)
    print(heigh_3)
    print(heigh_2)
elif heigh_3 >= heigh_1 and heigh_1 >= heigh_2:
    print(heigh_2)
    print(heigh_1)
    print(heigh_3)
else:
    print(heigh_1)
    print(heigh_2)
    print(heigh_3)