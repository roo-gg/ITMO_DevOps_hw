from datetime import datetime, timedelta
from pathlib import Path
import json
import random

from airflow.decorators import dag, task
from airflow.operators.python import get_current_context


@dag(
    dag_id="hw1_dag",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
    max_active_runs=1,
    default_args={"owner": "admin", "retries": 1, "retry_delay": timedelta(minutes=2)},
)
def hw1_dag():
    @task
    def make_data():
        ctx = get_current_context()
        ds = ctx["ds"]
        rnd = random.Random(int(ds.replace("-", "")))

        rows = []
        for i in range(1, 31):
            value = rnd.randint(10, 200)
            rows.append({"id": i, "value": value})
        return rows

    @task
    def calc_stats(rows):
        values = [row["value"] for row in rows]
        total = sum(values)
        avg = round(total / len(values), 2)
        max_value = max(values)
        min_value = min(values)
        return {
            "count": len(values),
            "sum": total,
            "avg": avg,
            "max": max_value,
            "min": min_value,
        }

    @task
    def check(stats):
        if stats["avg"] < 20:
            return {"status": "warn", "comment": "average is too low"}
        return {"status": "ok", "comment": "average is normal"}

    @task
    def save_report(stats, check_result):
        ctx = get_current_context()
        ds = ctx["ds"]

        report = {
            "date": ds,
            "stats": stats,
            "check": check_result,
        }

        report_dir = Path("/opt/airflow/reports")
        report_dir.mkdir(parents=True, exist_ok=True)
        path = report_dir / f"hw1_report_{ds}.json"
        path.write_text(json.dumps(report, indent=2), encoding="utf-8")
        return str(path)

    @task
    def print_result(path, check_result):
        print(f"report: {path}")
        print(f"status: {check_result['status']}")
        print(f"comment: {check_result['comment']}")

    rows = make_data()
    stats = calc_stats(rows)
    check_result = check(stats)
    path = save_report(stats, check_result)
    print_result(path, check_result)


hw1_dag()
