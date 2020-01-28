FROM python:3.6.5-jessie

WORKDIR /
COPY . /app

ENV ENV local
EXPOSE 5000

RUN adduser --disabled-password --gecos '' myuser

RUN chmod +x app/entrypoint.sh
RUN chmod +x app/entrypoint_beat.sh
RUN chmod +x app/entrypoint_worker.sh

RUN pip install -r /app/requeriments.txt