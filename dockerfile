FROM python:3.9.0

WORKDIR /TelegramBots/Footballbot

COPY requirements.txt /TelegramBots/Footballbot

RUN pip install -r requirements.txt 

COPY . /TelegramBots/Footballbot
