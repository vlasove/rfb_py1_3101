# Сортировка списка методом .sort()
words = ["alice", "bob", "aaa", "alex", "victor", "mister doctor professor", "ddd"]
words.sort() # Изменяется исходное состояние списка!

print("Words sorted ->:", words)
# Обратная сортировка (в обратном порядке)
words.sort(reverse=True)
print("Words sorted <-:", words)