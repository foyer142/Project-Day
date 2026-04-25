def get_done_tasks(tasks: list[dict]) -> list[dict]:
    return [task for task in tasks if task['done']]

def get_pending_tasks(tasks: list[dict]) -> list[dict]:
    return [task for task in tasks if not task['done']]

def get_task_titles(tasks: list[dict]) -> list[str]:
    return [task['title'] for task in tasks]

def sort_tasks_by_priority(tasks: list[dict]) -> list[dict]:
    return sorted(tasks, key=lambda task: task["priority"])

def add_task(tasks: list[dict], title: str, priority: int) -> list[dict]:
    tasks.append({'title': title,"done": False,'priority': priority})
    return tasks


tasks = [
    {"title": "learn python", "done": True, "priority": 2},
    {"title": "practice lists", "done": False, "priority": 1},
    {"title": "read about APIs", "done": False, "priority": 3},
    {"title": "clean project", "done": True, "priority": 2},
]

print("Done tasks:")
print(get_done_tasks(tasks))

print("Pending tasks:")
print(get_pending_tasks(tasks))

print("Task titles:")
print(get_task_titles(tasks))

print("Sorted by priority:")
print(sort_tasks_by_priority(tasks))

print("Add task:")
print(add_task(tasks.copy(), "write tests", 1))
