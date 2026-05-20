# CHANGES

## HW4

- Добавлены сервисы наблюдаемости: `loki`, `alloy`, `prometheus`, `grafana`.
- Добавлены внешние монтирования логов Spark:
  - `./spark-logs/master:/opt/spark/logs`
  - `./spark-logs/worker:/opt/spark/logs`
- Сохранено внешнее монтирование логов Airflow: `./logs:/opt/airflow/logs`.
- Добавлен конфиг метрик Spark `spark/conf/metrics.properties` с sink `PrometheusServlet`.
- Добавлен конфиг Alloy `monitoring/alloy/alloy.config` для сбора:
  - логов Airflow из `./logs`
  - логов Spark из `./spark-logs`
  и отправки в Loki.
- Добавлен конфиг Prometheus `monitoring/prometheus/prometheus.yml` для сбора метрик:
  - `spark-master`
  - `spark-worker`
  - `spark-applications`
- Добавлен provisioning Grafana:
  - источники данных (Prometheus + Loki)
  - provider для dashboard
  - дашборд `HW4 Spark Observability` с 2 панелями.
- Добавлены DAG и Spark job для HW4:
  - `dags/hw4_spark_dag.py`
  - `spark/hw4_metrics_job.py`

## Отличия относительно HW1/HW2/HW3

- HW1: базовый стек Airflow
- HW2: интеграция Spark и `SparkSubmitOperator`
- HW3: CI/CD пайплайн
- HW4: полноценный слой наблюдаемости (метрики + логи + дэшбод) поверх Airflow + Spark
