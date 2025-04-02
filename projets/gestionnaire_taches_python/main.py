import json

tasks = []

def add_task(title):
    tasks.append({"title": title, "done": False})
    print(f"Tâche '{title}' ajoutée.")

def list_tasks():
    for idx, task in enumerate(tasks, 1):
        status = "✓" if task["done"] else "✗"
        print(f"{idx}. {task['title']} [{status}]")

add_task("Apprendre Python")
add_task("Créer un projet")
list_tasks()
