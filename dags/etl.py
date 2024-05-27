from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
import sys
import os

sys.path.append('/opt/airflow/scripts')

from extract import extract_data
from transformation import transform_data
from load import load_data

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1
}

dag = DAG(
    'etl_processing',
    default_args=default_args,
    description='A simple ETL DAG',
    schedule_interval='@daily',
    start_date=days_ago(1),
    catchup=False
)

extract_task = PythonOperator(
    task_id='extract_data',
    python_callable=extract_data,
    dag=dag
)

transform_task = PythonOperator(
    task_id='transform_data',
    python_callable=transform_data,
    dag=dag
)

load_task = PythonOperator(
    task_id='load_data',
    python_callable=load_data,
    dag=dag
)

extract_task >> transform_task >> load_task
