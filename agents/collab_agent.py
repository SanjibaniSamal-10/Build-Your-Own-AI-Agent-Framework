from agents.reference_agent import run_reference_agent
from agents.research_agent import run_research_agent

def run_collaboration(input_text):
    ref_result = run_reference_agent(input_text)
    research_result = run_research_agent(ref_result['summary'])
    return {
        "reference_agent": ref_result,
        "research_agent": research_result
    }

def human_in_loop(input_text):
    summary = run_reference_agent(input_text)['summary']
    print("Please review the summary:", summary)
    confirm = input("Approve? (y/n): ")
    if confirm.lower() != 'y':
        summary = run_reference_agent(input_text + " revised")['summary']
    return summary