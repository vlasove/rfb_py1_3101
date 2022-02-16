# Решение задачи О
n_tasks = int(input())
tasks = []

for _ in range(n_tasks):
    tasks.append(input())

n_tasks_for_notion = int(input())
for _ in range(n_tasks_for_notion):
    num_task = int(input())
    print(tasks[num_task - 1])