"""
Создай класс Task, который позволяет управлять задачами (делами).
У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).
Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих
(не выполненных) задач.
"""

class Task():

    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        self.tasks.append({"description": description, "deadline": deadline,
                           "status": "Не выполнено"})

    def task_done(self, description):
        for task in self.tasks:
            if task["description"] == description:
                task["status"] = "Выполнено"
                print(f"Задача {description} выполнена!")
            elif task["description"] != description and task["status"] == "Не выполнено":
                pass
            else:
                print("Задача не найдена")

    def show_tasks(self):
        print("Текущие задачи:")
        for task in self.tasks:
            if task["status"] == "Не выполнено":
                print(f"{task["description"]} - {task["deadline"]}")

t = Task()
t.add_task("Уроки", "13.07.2024 17:00")
t.add_task("Тренировка", "14.07.2024 22:00")
t.add_task("Сон", "15.07.2024 08:00")

t.show_tasks()
t.task_done("Уроки")
t.task_done("Диван")
t.show_tasks()

