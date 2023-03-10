
FROM python:3.11

WORKDIR /rate_app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

