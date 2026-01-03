from agentflow.task import Task
from agentflow.flow import Flow
from agentflow.orchestrator import Orchestrator
from agentflow.memory import MemoryStore
from executors.search import SearchExecutor
from executors.summarize import SummarizeExecutor

def run_research_agent(user_input):
    flow = Flow("research_agent")
    flow.add_task(Task("search", "search"))
    flow.add_task(Task("summary", "summarize", deps=["search"]))
    flow.add_task(Task("insight", "summarize", deps=["summary"]))

    executors = {
        "search": SearchExecutor(),
        "summarize": SummarizeExecutor()
    }

    engine = Orchestrator(flow, executors, MemoryStore())
    return engine.run(user_input)