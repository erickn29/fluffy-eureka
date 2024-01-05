# Используем базовый образ Python
FROM python:3.12

# Устанавливаем poetry
RUN pip install poetry

# Создаем и переходим в рабочий каталог
WORKDIR /app

# Копируем файлы с зависимостями и файл pyproject.toml
COPY ../poetry.lock pyproject.toml /app/

# Устанавливаем зависимости с помощью poetry
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

# Копируем файлы приложения в рабочий каталог
COPY .. /app/

WORKDIR /app/backend

# Запускаем команду для запуска Django-приложения
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
