### Описание: ###
Тестовое задание для компании Ришат.

Из предложенных заданий выполнено:
- создана модель Item с полями name, description, price, currency;
- создан API с методами: `GET /buy/{id}`, `GET /item/{id}`, `GET order/<int:order_id>/` и `GET buy_order/<int:order_id>/`
- для хранения ключа stripe-api использованы переменные окружения;
- модели Item, Order, OrderItem зарегистрирована в панели Django Admin;
- решение залито на Github, запуск описан в Readme.md.
____

## Установка: ##

### Клонируйте репозиторий: ###
    git@github.com:mark-rom/rishat_assignment.git

### Перейдите в репозиторий в командной строке: ###
    cd stripe
  
### Создайте и активируйте виртуальное окружение: ###
    python3 -m venv venv

###### для Mac OS
    source venv/bin/activate

###### для Windows OS
    source venv/Scripts/activate
  
### Установите зависимости из файла requirements.txt: ###
### Обновите pip:
    python3 -m pip install --upgrade pip

### Установите зависимости:
    pip install -r requirements.txt

### Предоставьте переменные окружения: ###
Для работы API необходимо вручную создать .env файл с переменными окружения:
- STRIPE_API_KEY (Пример: sk_test_4eC39HqLyjWDarjtT1zdp7dc)
- DJANGO_SECRET_KEY (Пример: *_uep#-69ry%vf+hk_=%+*da&5!!csv64hi9wui+t$ft9=w!*e)
- DJANGO_DEBUG (Пример: True/False)

Обратите внимание, что stripe предоставляет два API key, в переменную окружения нужно внести `Secret key`.

### Выполните миграции: ###
    python3 manage.py migrate

### Создайте суперюзера: ###
    python3 manage.py createsuperuser

### Запустите проект: ###
    python3 manage.py runserver

### Заполните базу тестовыми данными: ###
Создайте несколько экземпляров Item, добавьте их в Order

### Запуск в Docker 
    docker build . -t image/name
    docker run -p 127.0.0.1:80:8000 image/name

После этого приложение будет доступно на локальной машине по адресу `127.0.0.1`