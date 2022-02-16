# Срезы
nums = [10, 20, 30, 40, 50]
print("Slice:", nums[1:4])
print("Reversed:", nums[::-1])
print("Each 2:", nums[::2])

sl = nums[::2]
for i in range(len(sl)):
    print(f"Id:{i} Elem:{sl[i]}")