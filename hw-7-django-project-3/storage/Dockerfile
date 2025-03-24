FROM postgres:13
ENV POSTGRES_USER=youruser
ENV POSTGRES_PASSWORD=yourpassword
ENV POSTGRES_DB=comments_db
COPY init.sql /docker-entrypoint-initdb.d/

FROM python:3.9-slim

WORKDIR /code

COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY django_project /code/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

