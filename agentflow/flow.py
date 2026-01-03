class Flow:
    def __init__(self, name):
        self.name = name
        self.tasks = {}

    def add_task(self, task):
        self.tasks[task.name] = task

    def topological_sort(self):
        visited = set()
        order = []

        def dfs(task_name):
            if task_name in visited:
                return
            visited.add(task_name)
            for dep in self.tasks[task_name].deps:
                dfs(dep)
            order.append(task_name)

        for task in self.tasks:
            dfs(task)

        return order