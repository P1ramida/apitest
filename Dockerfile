FROM python:3.11-slim

WORKDIR /app

# Копируем только необходимые файлы
COPY main.py utils.py ./

RUN pip install --no-cache-dir fastapi uvicorn

EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]