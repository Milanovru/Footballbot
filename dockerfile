FROM python:3.9.0

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app

RUN pip install -r requirements.txt /usr/src/app

COPY . /usr/src/app

CMD ["python3", "bot.py"]