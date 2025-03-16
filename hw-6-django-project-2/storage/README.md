# Инструкция по применению миграций

1. Создайте виртуальное окружение и установите зависимости:

pip install -r ../requirements.txt

2. Примените миграции:

python ../django_project/manage.py makemigrations python ../django_project/manage.py migrate

3. (Опционально) Загрузите тестовые данные:

python ../django_project/manage.py loaddata fixtures.json
