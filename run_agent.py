import time

def run_agent_flow(query: str):
    print("\n--- Agent Flow Started ---")

    context = {"query": query}

    # Planner Agent
    print("Planner Agent: routing task")
    time.sleep(0.1)

    # Search Agent
    print("Search Agent: searching for information")
    start = time.time()
    time.sleep(0.02)
    context["search_result"] = f"Information related to {query}"
    print(f"Executed search in {time.time() - start:.2f} sec")

    # Summary Agent
    print("Summary Agent: summarizing result")
    start = time.time()
    time.sleep(0.01)
    context["summary"] = f"{query} is a framework that enables agent orchestration."
    print(f"Executed summary in {time.time() - start:.2f} sec")

    # Collab Agent
    print("Collab Agent: coordinating agent outputs")
    start = time.time()
    time.sleep(0.01)
    context["final_answer"] = context["summary"]
    print(f"Executed collaboration in {time.time() - start:.2f} sec")

    print("--- Agent Flow Completed ---")

    #  FINAL ANSWER OUTPUT
    print("\n Final Answer:")
    print(context["final_answer"])
    print()

    return context["final_answer"]