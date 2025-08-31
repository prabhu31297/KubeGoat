FROM docker:dind

WORKDIR /app

COPY app.py .
COPY entrypoint.sh /entrypoint.sh

RUN apk add --no-cache python3 py3-flask bash curl && \
    chmod +x /entrypoint.sh


CMD ["/entrypoint.sh"]
