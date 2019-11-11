from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

# Defaults
default_args = {
    	'start_date': datetime(2019, 11, 11)
}

# DAGs
dag = DAG('HTTP_REQUEST', default_args=default_args, schedule_interval='05 9 * * *')

# Commands
bash_command = "/home/flume/hdfs_test/HTTP_2_HDFS.sh "

# Tasks
bash_task = BashOperator(
		task_id='HTTP',
		bash_command=bash_command,
		dag=dag
		)

# Node Connections
bash_task
