FROM python:3.8
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY ./api /app/api
COPY ./Project_API /app/Project_API
COPY ./manage.py /app/manage.py