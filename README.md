# СОЦИАЛЬНАЯ СЕТЬ API
### Описание
Этот проект является социальной сетью под названием YATUBE. Здесь можно публиковать записи, подписываться\отписываться на других юзеров, комментировать записи. Все это возможно в этом проекте, но пока через API. В фронтенд мы пока не особо умеем, но скоро чтото да появится)
------------------------------------------------------------
### Используемые библиотеки:
- [Python 3.7+](https://www.python.org/)
- [Django 2.2.16](https://www.djangoproject.com)
- [Django Rest Framework 3.12.4](https://www.django-rest-framework.org)
- [Djoser](https://djoser.readthedocs.io/en/latest/getting_started.html)
- [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
- [SQLite3](https://www.sqlite.org/index.html)
------------------------------------------------------------
### Установка:
#### *Действия для юзеров Windows**

Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/yandex-praktikum/kittygram.git
```
```
cd kittygram
```
Cоздать и активировать виртуальное окружение:
```
python -m venv env
```
```
source venv/Scripts/activate
```
Установить зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
Выполнить миграции:
```
python manage.py migrate
```
Запустить проект:
```
python manage.py runserver
```
------------------------------------------------------------
### Примеры запросов API

Для того чтобы создать публикацию, необходимо аутентифицироваться и использовать:
```
POST /api/v1/posts/
```
А в body передать значения `"text", "image", "group"`.

Для того чтобы обновить публикацию, юзаем:
```
PUT /api/v1/posts/{id}/
```
А в body передаем все теже `"text", "image", "group", "author"`.

