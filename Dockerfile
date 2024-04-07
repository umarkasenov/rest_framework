FROM python:3.10

ENV  PYTHONWRITEBYTCODE 1

WORKDIR /app

# . or /app/
COPY requirements.txt .

RUN pip install -r /app/requirements.txt

COPY . .
