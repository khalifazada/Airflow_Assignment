from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

# Defaults
default_args = {
    	'start_date': datetime(2019, 11, 11)
}

# DAGs
dag = DAG('FLUME_REQUEST', default_args=default_args, schedule_interval='* 9 * * *')

# Commands
flume_command = "flume-ng agent --name myAgent --conf-file ./http.conf "

# Tasks
flume_task = BashOperator(
    		task_id='FLUME',
		bash_command=flume_command,
    		dag=dag
)

# Node Connections
flume_task
