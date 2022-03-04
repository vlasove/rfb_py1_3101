# Пример считывания из JSON
import json

file_path = "data.json"

with open(file_path, "r") as fh:
    data = json.load(fh)

    print("Data type:", type(data))
    print("Data content:", data)