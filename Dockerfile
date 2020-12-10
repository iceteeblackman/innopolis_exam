FROM python:3.8.6-buster
MAINTAINER Kriukov Pavel
RUN apt-get update -y
RUN apt-get install -y gunicorn
RUN pip install --upgrade setuptools
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8003
CMD gunicorn -w 1 --reload start:app --bind 0.0.0.0:8003
