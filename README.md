# HW3: GitLab CI/CD

![Local check 1](screenshot1.png)
![Local check 2](screenshot2.png)
![Local check 3](screenshot3.png)
![Local check 4](screenshot4.png)

## Как проверить локально
```powershell
docker compose up -d --build
docker compose ps
curl http://localhost:8000/
```

Остановить сервис:
```powershell
docker compose down -v --remove-orphans
```

## Что реализовано по заданию
- Stage `test` выполняется всегда (`rules: when: always`).
- `build` не стартует автоматически для `feature/*` (ручной запуск).
- `deploy` автоматически только для `main/master/develop`.
- Все job запускаются только на тегированном runner (`default.tags: [hw3-runner]`).

## Локальный GitLab Runner (опционально)
Файл для запуска раннера: `runner/docker-compose.runner.yml`.

```powershell
docker compose -f docker-compose.runner.yml up -d
```

Runner должен иметь тег hw3-runner.

