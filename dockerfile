FROM python:3.9.0

WORKDIR /src

COPY requirements.txt /src

RUN pip install -r requirements.txt /src

COPY . /src

CMD ["python3", "bot.py"]