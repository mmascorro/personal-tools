FROM python:3.10.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY requirements/ /requirements/
RUN pip install -r /requirements/dev.txt