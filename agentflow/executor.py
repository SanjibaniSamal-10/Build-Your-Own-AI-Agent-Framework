class BaseExecutor:
    def execute(self, context):
        raise NotImplementedError("Executor must implement execute()")