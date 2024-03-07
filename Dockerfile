# syntax=docker/dockerfile:1

FROM python:3.10.9-slim-bullseye

WORKDIR /main
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

CMD [ "python3","main.py"]

