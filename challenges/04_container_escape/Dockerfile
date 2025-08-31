FROM python:3.9-slim

WORKDIR /app
COPY app.py .
COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh && pip install flask

ENTRYPOINT ["/entrypoint.sh"]
