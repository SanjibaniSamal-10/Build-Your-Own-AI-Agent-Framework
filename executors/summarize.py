from agentflow.executor import BaseExecutor

class SummarizeExecutor(BaseExecutor):
    def execute(self, context):
        return f"Summary of ({context['search']})"