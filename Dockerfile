FROM python:3.9-slim
WORKDIR /app
RUN pip install flask
RUN pip install g4f
COPY . .
# Команда для запуска приложения (например, Flask)
CMD ["python", "main.py"]