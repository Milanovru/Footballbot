FROM python:3.9.0

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt 

COPY . /app
