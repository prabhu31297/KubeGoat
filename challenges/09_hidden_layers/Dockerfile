FROM python:3.9-slim


RUN echo "FLAG{hidden_layers_flag_stealth}" > /hidden_flag.txt

RUN rm /hidden_flag.txt

WORKDIR /app
COPY app.py .
RUN pip install flask
CMD ["python", "app.py"]
