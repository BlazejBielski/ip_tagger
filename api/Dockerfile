FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

WORKDIR /app

COPY ./requirements.txt /app/

RUN apt-get update && apt-get install -y netcat-traditional

COPY ./scripts/entrypoint.sh .

COPY . .

ENTRYPOINT ["./entrypoint.sh"]