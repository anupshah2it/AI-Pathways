FROM python:3.11-slim
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["python", "-m", "cli.main", "start", "--config", "channels.json"]
