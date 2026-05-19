# HW1 Airflow

DAG делает:
1. Генерирует тестовый набор чисел
2. Считает базовые метрики (sum, avg, min, max)
3. Проверяет условие по среднему
4. Сохраняет отчет в `reports/hw1_report_YYYY-MM-DD.json`
5. Пишет результат в лог

## Как запускать

```powershell
git clone <repo_url>
cd <repo_name>
docker compose up -d --build
```

UI Airflow: `http://localhost:8080`
Логин/пароль: `admin` / `admin`
