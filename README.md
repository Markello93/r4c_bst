# R4C - Robots for consumers
## Описание
Cервис, который способен вести учет произведенных роботов, формировать еженедельные отчеты и оповещать клиентов, когда интересующий их робот появляется в наличии.

Сервис состоит из трех приложений:
- robots - наполнение базы данных данными о произведенных роботах и формирование еженедельного отчета
- orders - формирование заказов
- customers - данные клиентов

## Установка
```
git clone https://github.com/Markello93/r4c_bst.git
```
```
cd R4C
```
Установить зависимости и активировать виртуальное окружение c помощью poetry:
```
poetry install
```
```
source .venv/Scripts/activate
```
Или установить зависимости и активировать виртуальное окружение c помощью pip:
```
python -m venv venv
```
```
source venv/Scripts/activate
```
```
pip install requirements.txt
```
Выполнить миграции:
```
python manage.py migrate
```

Создать суперпользователя:
```
python manage.py makemigrations
```
Выполнить импорт тестовых данных о произведенных роботах в базу данных (при необходимости):
```
python manage.py fill_database
```
Запустить проект:
```
python manage.py runserver
```

## Реализация задач прописанных в файле tasks.md
### Task 1.
Добавление в БД робота осуществляется путем отправки POST запроса на endpoint:
http://127.0.0.1:8000/robots/add_robot/
Пример входных данных согласно заданию:
```{"model":"R2","version":"D2","created":"2022-12-31 23:59:59"}```
### Task 2.
Для формирования недельного отчета необходимо отправить GET запрос на endpoint:
http://127.0.0.1:8000/robots/week_report/

###Task 3.
Для формирования заказа необходимо отправить POST запрос на endpoint:
Пример входных данных:
```{"model":"R2","version":"D2","email":"example@mail.com"}```
http://127.0.0.1:8000/orders/make_order/

Если робот есть в базе, то заказ успешно создаться и робот забронируется флагом "ordered"
Если робота нет в базе, то при добавлении робота с необходимой моделью
отправится письмо на почту.

Для работы с почтовым сервером нужно создать .env файл с переменными:
```
EMAIL_HOST_USER = email  для аутентификации на SMTP-сервере
EMAIL_HOST_PASSWORD = пароль для вашей учетной записи на SMTP-сервере
EMAIL_HOST = адрес SMTP-сервера
```

Также, для тестирования отправки сообщения с уведомлением в консоль,
а не через SMTP-сервер,
в файле settings.py оставлена закомментированная настройка:
```
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```
Необходимо раскомментировать ее и закомментировать
```
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
```
