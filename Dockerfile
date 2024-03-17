FROM python:3.9.6-slim-buster

# Install required library libmysqlclient (and build-essential for building mysqlclient python extension)
RUN set -eux && \
    export DEBIAN_FRONTEND=noninteractive && \
    apt-get update && \
    apt-get install -y default-libmysqlclient-dev build-essential wget && \
    rm -rf /var/lib/apt/lists/*

ENV PYTHONUNBUFFERED = 0
ENV POETRY_VERSION=1.3.2

COPY . /app
WORKDIR /app

RUN pip install pip --upgrade && \
    pip install "poetry==$POETRY_VERSION"
RUN poetry export -o requirements.txt --without-hashes --dev && \
    pip install -r requirements.txt

ENTRYPOINT ["make", "run-server"]