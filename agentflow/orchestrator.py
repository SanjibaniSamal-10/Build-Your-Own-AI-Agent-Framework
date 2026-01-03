import time
import threading
from agentflow.guardrails import Guardrails
from agentflow.observability import Logger, Metrics

class Orchestrator:
    def __init__(self, flow, executors, memory):
        self.flow = flow
        self.executors = executors
        self.memory = memory
        self.guardrails = Guardrails()
        self.logger = Logger()
        self.metrics = Metrics()

    def _execute_task(self, task, context):
        """Execute task with retries and timeout"""
        for attempt in range(task.retries + 1):
            try:
                output_container = {}
                thread = threading.Thread(
                    target=lambda: output_container.update({'result': self.executors[task.tool].execute(context)})
                )
                thread.start()
                thread.join(task.timeout)
                if thread.is_alive():
                    raise TimeoutError(f"Task {task.name} timed out after {task.timeout}s")
                output = output_container['result']

                self.guardrails.validate(output)
                return output
            except Exception as e:
                self.logger.log(f"Task {task.name} failed on attempt {attempt+1}: {e}")
                if attempt == task.retries:
                    raise e

    def run(self, input_data):
        context = {"input": input_data}

        for task_name in self.flow.topological_sort():
            task = self.flow.tasks[task_name]
            start = time.time()
            output = self._execute_task(task, context)
            duration = time.time() - start

            self.memory.save(task_name, output)
            context[task_name] = output
            self.metrics.record(task_name, duration)
            self.logger.log(f"Executed {task_name} in {duration:.2f}s")

        return context