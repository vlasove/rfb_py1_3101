# Сортировка с сохранением исходного списка
words = ["alice", "bob", "aaa", "alex", "victor", "mister doctor professor", "ddd"]
new_words_sorted_primary = sorted(words)

print("Origin words:", words)
print("sorted words:", new_words_sorted_primary)

# Обратный порядок сортировки
new_words_sorted_reversed = sorted(words, reverse=True)
print("sorted reversed:", new_words_sorted_reversed)
print("Origin words:", words)