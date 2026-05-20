# CHANGES

## HW3
- Добавлен `.gitlab-ci.yml` с этапами `test/build/deploy`.
- Добавлены правила веток:
  - test: всгда
  - build: manual для `feature/*`
  - deploy: только `main/master/develop`
- Добавлен tag-filter для runner: `hw3-runner`.
- Добавлен ручной job `clear-service` для очистки окружения.
- Подготовлен минимальный докер-сервис для проверки депляо.
- Добавлен `runner/docker-compose.runner.yml` для локального запуска GitLab Runner.
- По сравнению с HW1/HW2 добавлен CI/CD пайплайн GitLab и правила запуска job по веткам/runner tag.
- Для отчета подготовлены 4 скриншота:
  - локальная проверка `docker compose ps`,
  - локальная проверка `curl http://localhost:8000/`,
  - успешный pipeline в GitLab,
  - лог job `test-structure` с прохождением синтетического теста.