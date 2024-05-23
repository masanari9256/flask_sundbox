FROM --platform=linux/amd64 python:3.11

WORKDIR /var/www/app

COPY . .

RUN pip install -U pip \
    && pip install --no-cache-dir -r /var/www/app/config/requirements.txt
