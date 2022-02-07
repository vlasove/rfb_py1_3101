# Решение задачи K

LOW_PULSE_VALUE, BIG_PULSE_VALUE = 100, 140
MAX_PULSE = -1
MIN_PULSE = 141
count = 0

while True:
    pulse = float(input())
    if pulse < 0:
        break
    if pulse >= LOW_PULSE_VALUE and pulse <= BIG_PULSE_VALUE:
        count += 1
        if pulse > MAX_PULSE:
            MAX_PULSE = pulse
        if pulse < MIN_PULSE:
            MIN_PULSE = pulse

print(count)
print(MIN_PULSE, MAX_PULSE)