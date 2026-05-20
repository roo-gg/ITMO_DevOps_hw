from __future__ import annotations

import json
import random
import sys
from pathlib import Path
from typing import List, Tuple

from pyspark.sql import SparkSession
from pyspark.sql import functions as F


def _build_rows(seed: int) -> List[Tuple[int, str, int]]:
    rnd = random.Random(seed)
    categories = ["python", "sql", "devops", "ml", "etl"]

    rows: List[Tuple[int, str, int]] = []
    for idx in range(1, 301):
        category = categories[idx % len(categories)]
        score = rnd.randint(30, 100)
        rows.append((idx, category, score))
    return rows


def main() -> None:
    ds = sys.argv[1] if len(sys.argv) > 1 else "unknown-date"
    seed = int(ds.replace("-", "")) if ds != "unknown-date" else 1

    spark = (
        SparkSession.builder.appName("hw4_metrics_job")
        .master("spark://spark-master:7077")
        .getOrCreate()
    )

    rows = _build_rows(seed)
    df = spark.createDataFrame(rows, schema=["id", "category", "score"])

    metrics_df = (
        df.groupBy("category")
        .agg(
            F.count("*").alias("records"),
            F.round(F.avg("score"), 2).alias("avg_score"),
            F.max("score").alias("max_score"),
            F.min("score").alias("min_score"),
        )
        .orderBy("category")
    )

    summary = {
        "date": ds,
        "total_rows": df.count(),
        "global_avg_score": round(df.agg(F.avg("score")).first()[0], 2),
        "by_category": [row.asDict() for row in metrics_df.collect()],
    }

    out_dir = Path("/opt/airflow/reports")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / f"hw4_spark_report_{ds}.json"
    out_file.write_text(json.dumps(summary, indent=2), encoding="utf-8")

    print(f"Spark report saved to: {out_file}")
    spark.stop()


if __name__ == "__main__":
    main()
