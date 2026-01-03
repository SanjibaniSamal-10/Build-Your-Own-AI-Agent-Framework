from agentflow.executor import BaseExecutor

class SearchExecutor(BaseExecutor):
    def execute(self, context):
        return f"Search results for: {context['input']}"