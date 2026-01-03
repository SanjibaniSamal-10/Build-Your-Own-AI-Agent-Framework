from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from run_agent import run_agent_flow

with DAG(
    dag_id="agentflow_orchestration",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False
) as dag:

    run_agent = PythonOperator(
        task_id="run_agentflow",
        python_callable=run_agent_flow,
        op_args=["AI Agents"]
    )