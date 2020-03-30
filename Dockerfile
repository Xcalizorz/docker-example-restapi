FROM python:3.7.7-alpine
COPY app /app

WORKDIR /app

RUN pip3 install --upgrade pip \
    && pip3 install -r requirements.txt

EXPOSE 5000
ENTRYPOINT ["python3", "app.py"]
