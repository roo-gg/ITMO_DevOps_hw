# CHANGES

## Lab 2 changes (relative to Lab 1)

- Added Spark standalone cluster services: `spark-master`, `spark-worker`.
- Added `spark` directory with spark job script.
- Extended `Dockerfile` with:
  - `USER root` for apt-based package install;
  - install of `procps` and `default-jre`;
  - return to `USER airflow`;
  - install of `apache-airflow-providers-apache-spark`.
- Added DAG with `SparkSubmitOperator` to run spark job.
- Added Spark volume mount `./spark:/opt/airflow/spark`.
- Added report generation from Spark job into `reports/`.
