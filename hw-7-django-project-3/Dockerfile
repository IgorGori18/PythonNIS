FROM python:3.9-slim

WORKDIR /app

COPY django_project/requirements.txt /app/


RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /app/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
