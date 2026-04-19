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

## CI/CD Pipeline

### Триггер
**Автоматический запуск при push в ветку `main`**

### Что делает пайплайн

1. Checkout кода
2. Логин в Docker Hub
3. Сборка Docker образа
4. Push образа в registry
5. SSH подключение к VPS
6. Pull нового образа
7. Перезапуск контейнеров (`docker compose up -d`)

### Секреты GitHub Actions

| Секрет | Назначение |
|--------|------------|
| `DOCKER_USERNAME` | Логин Docker Hub |
| `DOCKER_PASSWORD` | Токен доступа Docker Hub |
| `VPS_HOST` | IP адрес VPS |
| `VPS_USER` | Пользователь на VPS |
| `VPS_SSH_KEY` | Приватный SSH ключ |
