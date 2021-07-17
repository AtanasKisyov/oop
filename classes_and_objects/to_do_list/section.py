class Section:

    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
                return f"Completed task {task.name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        current_tasks = len(self.tasks)
        self.tasks = [x for x in self.tasks if not x.completed]
        remaining_tasks = len(self.tasks)
        return f"Cleared {current_tasks - remaining_tasks} tasks."

    def view_section(self):
        string_to_return = ""
        for t in self.tasks:
            string_to_return += f"{t.details()}\n"
        string_to_return = string_to_return[:-1]
        return f"Section {self.name}:\n{string_to_return}"
