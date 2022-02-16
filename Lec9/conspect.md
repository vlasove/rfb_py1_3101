## Лекция 9. Списки. Продолжение

### 1. Методы списков
```
# Методы списков
numerics = [10, 20, 30, 40, 30, 30]
print(dir(numerics))

# 1) Списки - ссылочный тип!
b = numerics[:] #numerics.copy()
b.append(9999999)
print("Numerics:", numerics)
print("b:", b)

# 2) .count() - подсчет количества вхождений
print("30 in in numerics:", numerics.count(30))

# 3) .extend() - подшивает другой список в конец исходного
numerics.extend([9999, 99,9999])
print(".extend():", numerics)

# 4) .index()
print(".index():", numerics.index(30))

# 5) .reverse()
numerics.reverse()
print(".reverse():", numerics)
```

### 2. Методы преобразования str-list
```
# Строковый метод .split()
message = "Bob likes Python programming"
words = message.split(sep=" ")
print("Words:", words)

# Строковый метод .join()
output_str = ", ".join(words) # "Bob" + "\n" + "likes" + "\n" + "Python" +\n" + "programming"
print(output_str)

# .join() работает только с list[str]
nums = [10, 20, 30]
for i in range(len(nums)):
    nums[i] = str(nums[i])

print(", ".join(nums))
```

* `.split(sep="str") -> lst[str]` - метод (строки), который разбивает строку на набор подстрок по указанному сепаратору и возвращает список подстрок!

* `"sep".join(lst[str]) -> str` - метод (строки), который принимает на вход список подстрок и конкатенирует все элементы через указанный сепаратор - возвращает одну большую строку.

### 4. Преобразование str-set-list
* `list-set`
```
numerics_list = [10, 10, 20, 20, 30, 30, 40, 40, 50, 50]
numerics_set = set(numerics_list) # Преобразование из списка в множество
new_list = list(numerics_set) # Преобразование из множества в список

numerics_list = sorted(list(set(numerics_list)))
print(numerics_list)
```

* `list-str`
```
words = "Hello world"
letters = list(words)
print(letters)

print("".join(["10", "20"]))
```