FROM python:3.7.0

RUN apt-get update
RUN apt-get install -y python3-dev python-dev
RUN pip install --upgrade pip

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /usr/src
