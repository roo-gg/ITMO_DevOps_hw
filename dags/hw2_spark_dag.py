from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator


default_args = {
    "owner": "admin",
    "retries": 1,
    "retry_delay": timedelta(minutes=2),
}


with DAG(
    dag_id="hw2_spark_dag",
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
    max_active_runs=1,
    tags=["hw2", "spark"],
) as dag:
    start = EmptyOperator(task_id="start")

    run_spark_job = SparkSubmitOperator(
        task_id="run_spark_job",
        conn_id="spark_local",
        application="/opt/airflow/spark/hw2_metrics_job.py",
        name="hw2_metrics_job",
        application_args=["{{ ds }}"],
        conf={
            "spark.master": "spark://spark-master:7077",
            "spark.submit.deployMode": "client",
            "spark.driver.host": "airflow-scheduler",
            "spark.driver.bindAddress": "0.0.0.0",
        },
        verbose=False,
    )

    finish = EmptyOperator(task_id="finish")

    start >> run_spark_job >> finish
