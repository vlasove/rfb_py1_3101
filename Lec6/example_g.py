# Решение задачи S
bus_forward = set()
bus_backward = set()
##########
while True:
    bus = input()
    if bus == "":
        break
    bus_forward.add(bus)

while True:
    bus = input()
    if bus == "":
        break
    bus_backward.add(bus)
##########
common_bus = bus_forward.intersection(bus_backward)
print(len(common_bus))