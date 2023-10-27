from typing import List
from project.task import Task


class Section:

    def __init__(self, name: str):
        self.name = name
        self.tasks: List[Task] = []

    def add_task(self, new_task: Task) -> str:

        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"

        self.tasks.append(new_task)

        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):

        for current_task in self.tasks:

            if current_task.name == task_name:
                current_task.completed = True

                return f"Completed task {task_name}"

        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        completed_tasks = 0

        for current_task in self.tasks:

            if current_task.completed:

                completed_tasks += 1
                self.tasks.remove(current_task)

        return f"Cleared {completed_tasks} tasks."

    def view_section(self):
        tasks_details = "\n".join([current_task.details() for current_task in self.tasks])

        return f"Section {self.name}:\n" +\
               f"{tasks_details}"
      
