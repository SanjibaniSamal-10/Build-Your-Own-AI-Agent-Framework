class Task:
    def __init__(self, name, tool, deps=None, retries=2, timeout=10):
        self.name = name
        self.tool = tool
        self.deps = deps or []
        self.retries = retries
        self.timeout = timeout