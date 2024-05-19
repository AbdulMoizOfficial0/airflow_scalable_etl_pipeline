from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys
import os

# Adding the scripts directory to PATH
sys.path.insert(0, '/opt/airflow/scripts')

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'etl_dag',
    default_args=default_args,
    description='A simple scalable ETL process',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2023, 1, 1),
    catchup=False,
)

def extract():
    from extract import extract_data
    extract_data()

def transform():
    from transform import transform_data
    transform_data()

def load():
    from load import load_data
    load_data()

extract_task = PythonOperator(
    task_id='extract_task',
    python_callable=extract,
    dag=dag,
)

transform_task = PythonOperator(
    task_id='transform_task',
    python_callable=transform,
    dag=dag,
)

load_task = PythonOperator(
    task_id='load_task',
    python_callable=load,
    dag=dag,
)

extract_task >> transform_task >> load_task
