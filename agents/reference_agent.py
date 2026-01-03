from agentflow.task import Task
from agentflow.flow import Flow
from agentflow.orchestrator import Orchestrator
from agentflow.memory import MemoryStore
from executors.search import SearchExecutor
from executors.summarize import SummarizeExecutor

def run_reference_agent(user_input):
    flow = Flow("reference_agent")
    flow.add_task(Task("search", "search"))
    flow.add_task(Task("summary", "summarize", deps=["search"]))

    executors = {
        "search": SearchExecutor(),
        "summarize": SummarizeExecutor()
    }

    engine = Orchestrator(flow, executors, MemoryStore())
    return engine.run(user_input)