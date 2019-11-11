from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator, BranchPythonOperator
from datetime import datetime

# Defaults
default_args = {
    	'start_date': datetime(2019, 11, 11),
	'depends_on_past':True
}

# DAGs
dag = DAG('HTTP_2_HDFS', default_args=default_args, schedule_interval='59 * * * *')

# Commands
flume_command = "flume-ng agent --name myAgent --conf-file /home/hadoop/flume/conf/http.conf "

sleep_command = "sleep 30 "

bash_command = "/home/flume/hdfs_test/HTTP_2_HDFS.sh "

# Tasks
dummy_task = DummyOperator(
    		task_id='DUMMY',
    		dag=dag,
)

flume_task = BashOperator(
    		task_id='FLUME',
		bash_command=flume_command,
    		dag=dag
)

sleep_task = BashOperator(
		task_id='SLEEP',
	    	bash_command=sleep_command,
	   	dag=dag
		)

bash_task = BashOperator(
		task_id='HTTP',
		bash_command=bash_command,
		dag=dag
		)

def my_func():
	return ['SLEEP', 'HTTP']

branch = BranchPythonOperator(task_id='BRANCH', python_callable=my_func, dag=dag)

# Node Connections
branch >> dummy_task >> flume_task
branch >> sleep_task >> bash_task



