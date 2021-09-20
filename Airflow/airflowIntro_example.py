import datetime as dt
from datetime import timedelta

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

import pandas as pd

def CSVtoJSON():
    df=pd.read_csv('data.csv')
    for i,r in df.iterrows():
        print(r['name'])
    df.to_json('jsonData.JSON', orient='records')

default_args = {
    'owner': 'SamSchultz',
    'start_date': dt.datetime(2021,9,20),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=5)
}

with DAG('MyCSVDAG', 
        default_args=default_args,
        schedule_interval=timedelta(minutes=5)
        ) as dag:
            print_starting = BashOperator(task_id='starting', bash_command = 'echo "Reading the CSV now..."')

            CSVJson = PythonOperator(task_id='convertCSVtoJson', python_callable=CSVtoJSON)

            print_starting >> CSVJson
            CSVJson << print_starting