# Решение задачи B
n = int(input().strip())
queue = []

for _ in range(n):
    event_message = input().strip()
    if "Кто последний" in event_message:
        # Кто последний? Я - Кузнецов.
        last_name_with_dot_str = event_message.split(sep= " - ")[-1] # ["Кто последний? Я", "Кузнецов."][-1] -> "Кузнецов."
        last_name = last_name_with_dot_str.split(sep=".")[0] # ["Кузнецов", ""][0]
        queue.append(last_name)
    elif "Я только спросить" in event_message:
        last_name_with_dot_str = event_message.split(sep= " - ")[-1] # ["Я только спросить! Я", "Кузнецов."][-1] -> "Кузнецов."
        last_name = last_name_with_dot_str.split(sep=".")[0] # ["Кузнецов", ""][0]
        queue.insert(0, last_name)
    elif "Следующий" in event_message:
        if len(queue) == 0:
            print("В очереди никого нет.")
        else:
            next_person = queue.pop(0) #
            print(f"Заходит {next_person}!")