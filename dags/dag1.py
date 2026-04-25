from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from airflow.operators.email import EmailOperator

def process_transactions_logic():
    transactions = [120, 300, 450, 200]
    total = sum(transactions)
    count = len(transactions)
    
    report_content = (
        f"Daily Transaction Report\n"
        f"Number of transactions: {count}\n"
        f"Total amount: {total}"
    )
    
    with open("/data/transactions_report.txt", "w") as f:
        f.write(report_content)

with DAG(
    dag_id="Report_Transaction_Pipeline",
    start_date=datetime(2026, 4, 7),
    schedule_interval=timedelta(minutes=10),
    catchup=False,
) as dag:

    start_task = PythonOperator(
        task_id='print_start',
        python_callable=lambda: print(f"Transaction pipeline started at {datetime.now()}")
    )

    process_task = PythonOperator(
        task_id='calculate_transactions',
        python_callable=process_transactions_logic
    )

    run_script_task = BashOperator(
        task_id='run_external_script',
        bash_command='python3 /opt/airflow/plugins/app.py'
    )

    send_email_task = EmailOperator(
        task_id='send_email_report',
        to='yousef.said211@gmail.com',
        subject='Transaction Report',
        html_content="/data/transactions_report.txt" 
    )

    start_task >> process_task >> run_script_task >> send_email_task