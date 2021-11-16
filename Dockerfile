FROM python:3 as dev
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY . /app

FROM dev
RUN pip install gunicorn