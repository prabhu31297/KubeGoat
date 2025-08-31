FROM python:3.9-slim
WORKDIR /app
COPY app.py .
COPY kubelet.conf .
RUN pip install flask
CMD ["python", "app.py"]
