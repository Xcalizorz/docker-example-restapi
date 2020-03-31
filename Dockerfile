FROM python:3.7.7-alpine
WORKDIR /learn_docker_app
COPY learn_docker_app ./

RUN pip3 install --upgrade pip \
    && pip3 --disable-pip-version-check --no-cache-dir install -r requirements.txt \
    && pip3 --disable-pip-version-check --no-cache-dir install -r requirements-test.txt \
    && rm -r *.txt \
    && pytest

EXPOSE 5000
ENTRYPOINT ["python3", "app.py"]
