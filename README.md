# Для запуска проекта необходимо

Операционная система: Ubuntu 20.04

База данных: Postgres 12

Django 4, python 3.8 >

```shell
python3 -m pip install virtualenv && python3 -m virtualenv venv && source venv/bin/activate
```
```shell
pip install -r requirements.txt
```

## Для заполения fixture
Иcпользуйте приведенные команды в заданном порядке

```bash
python manage.py loaddata catalog/fixtures/genre.json
```
```bash
python manage.py loaddata catalog/fixtures/author.json
```
```bash
python manage.py loaddata catalog/fixtures/book.json
```
```bash
python manage.py loaddata catalog/fixtures/bookinstance.json
```
