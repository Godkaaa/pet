![GitHub Actions](https://github.com/Godkaa/devops-pet-project/actions/workflows/deploy.yml/badge.svg)

## О проекте

Учебный проект для портфолио

### Что умеет приложение?
- `GET /`  приветствие + счётчик запросов (хранится в Redis)
- `GET /health`  проверка здоровья сервиса
- `GET /metrics`  метрики (общее число запросов)

### Цели проекта
- Показать понимание контейнеризации и CI/CD
- Создать автоматизированный пайплайн "от коммита до продакшена"

---

---

##  Технологии

| Компонент | Технология |
|-----------|------------|
| Backend | FastAPI (Python 3.11) |
| База данных | Redis 7 |
| Web сервер | Nginx (reverse proxy) |
| Контейнеризация | Docker + Docker Compose |
| CI/CD | GitHub Actions |
| Registry | Docker Hub |
| Сервер | VPS (Ubuntu) |
| Версионирование | Git |

---
