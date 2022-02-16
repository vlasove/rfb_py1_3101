# Строковый метод .split()
message = "Bob likes Python programming"
words = message.split(sep=" ")
print("Words:", words)

# Строковый метод .join()
output_str = ", ".join(words) # "Bob" + ", " + "likes" + ", " + "Python" +", " + "programming"
print(output_str)

# .join() работает только с list[str]
nums = [10, 20, 30]
for i in range(len(nums)):
    nums[i] = str(nums[i]) # str(10) => "10"

print(", ".join(nums)) # "10" + ", " + "20" + ", " + "30"