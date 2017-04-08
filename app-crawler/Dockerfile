FROM python:3.3.6-slim
MAINTAINER Otavio Braga <braganantes@gmail.com>

RUN groupadd -r app-crawler && useradd -r -g app-crawler app-crawler

RUN mkdir -p /app-crawler
WORKDIR /app-crawler
COPY . /app-crawler
RUN chown -R app-crawler /app-crawler

RUN pip install -r requirements.txt