import time

class Logger:
    def log(self, message):
        print(f"[LOG] {time.ctime()} - {message}")

class Metrics:
    def __init__(self):
        self.records = []

    def record(self, task_name, duration):
        self.records.append({
            "task": task_name,
            "duration": duration
        })