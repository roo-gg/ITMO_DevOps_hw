FROM apache/airflow:2.7.1

WORKDIR /opt/airflow

USER root
RUN apt-get update \
    && apt-get install -y --no-install-recommends procps default-jre \
    && rm -rf /var/lib/apt/lists/*

USER airflow
RUN pip install --no-cache-dir apache-airflow-providers-apache-spark \
    --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.7.1/constraints-3.8.txt"

COPY dags/ /opt/airflow/dags/
COPY spark/ /opt/airflow/spark/
