FROM --platform=linux/amd64 nginx:latest

RUN apt-get update \
    && apt-get install -y vim \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*
