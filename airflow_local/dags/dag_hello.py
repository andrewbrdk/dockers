from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

dag = DAG('hello_world', 
          description='Hello World DAG',
          schedule_interval='*/1 * * * *',
          start_date=datetime(2023, 9, 1), 
          catchup=False)

hello = BashOperator(
            dag=dag,
            task_id='hello_task', 
            bash_command='echo Hello world!')

hello
