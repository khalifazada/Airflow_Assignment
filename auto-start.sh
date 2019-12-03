#!/bin/bash

# start Airflow webserver in daemon
airflow webserver -D

# start Airflow scheduler in daemon
airflow scheduler -d
