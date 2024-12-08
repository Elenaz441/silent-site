# О проекте
Тема: Сайт для знакомств людей, которые ищут друг друга для молчания

Макеты: https://www.figma.com/design/AyoEw6pwZeO6LJy8BCq8rf/Untitled?node-id=0-1&node-type=canvas&t=WGs3h4WaVap3dXjU-0

# Запуск кода

## Настройка переменных окружения
Для начала нужно создать файл .env в папке silent-site и в папке src. Скопировать содержимое файлов .env.template в соответствующие по уровню файлы .env.

## Создание, активация и настройка виртуальной среды
```bash
python -m venv .venv
.venv\Scripts\activate.bat
pip install -r requirements.txt
```

## Установка базы данных
Для работы приложения нужна СУБД PostgreSQL. Для её установки можно использовать docker-compose.

```bash
docker-compose up -d
```

## Создание таблиц

```bash
cd src
alembic upgrade head
```

## Запуск

```bash
uvicorn main:app --reload
```

Если всё сделано правильно, то должна быть доступна ссылка http://127.0.0.1:8000/docs.
Там представлена документация по маршрутам.

# О коде
[main.py](src/main.py) - здесь создается и запусткается приложение.

[database.py](src/database.py) - здесь создается сессия для подключения к бд.

[config.py](src/config.py) - здесь настройки приложения.

[schemas](src/schemas) - пакет с DTO. Если кратко, DTO - это то, в каком виде данные должны приходить в приложение или отправляться из него.

[models](src/models) - пакет с моделями бд (как данные хранятся в бд).

[api](src/api) - пакет с роутерами/маршрутами.