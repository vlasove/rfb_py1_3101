"""
Анонимные функции, примеры
"""
# from typing import Tuple
# def my_key(word:str) -> Tuple[int, str]:
#     """
#     Ключ для сортировки строкового списка
#     """
#     print("Current word:", word)
#     return (len(word), word)

def main():
    """
    entry point
    """
    words = ["alice", "a","beb", "aaa", "bob", "josh", "george", "penny", "leonard", "alex"]
    words.sort(key=lambda word: (len(word),word)) # [(len("alice"), "alice"), (len('a'), 'a'), (len("beb"), "beb"), (len("aaa"), "aaa"), ...]
    #word.sort(key=my_key)
    print(words)

main()
