# Local Library (Django)

|[English version](https://github.com/KonstErz/test_website_django_-locallibrary-/blob/master/README.md)|

Это небольшой учебный веб-сайт, написанный на Django.
Он был создан в рамках туториала по Django от [MDN web docs](https://developer.mozilla.org/ru/docs/Learn/Server-side/Django).


## Особенности

Данное веб-приложение создает онлайн-каталог для небольшой местной библиотеки, где пользователи могут просматривать доступные книги и управлять своими учетными записями.

Основные функции, которые были реализованы в настоящее время:

+ Есть модели для книг, экземпляров книг, авторов, жанров и языков.
+ Пользователи могут просматривать список книг и авторов и подробную информацию о них.
+ Администратор может создавать модели и управлять ими. Администрирование было оптимизировано.
+ Библиотекари (пользователи со статусом «Сотрудник») могут обновлять зарезервированные книги, а также создавать новых авторов и книги, обновлять данные о них или удалять их.
+ Этот веб-сайт развернут на свободном сервере Heroku.

## Быстрый старт

Вы можете запустить этот проект локально на вашем компьютере, выполнив следующие действия:

1. Настройте [среду разработки Python](https://developer.mozilla.org/ru/docs/Learn/Server-side/Django/development_environment). Рекомендуется использовать виртуальную среду разработки Python.
2. После того, как вы убедились, что Python корректно установлен на ваш компьютер, из корневой директории проекта выполните следующие команды в терминале (если вы работаете в Windows, вы можете использовать команды `py` или `py -3` вместо `python` для запуска Python):
    
    pip3 install -r requirements.txt
    python3 manage.py makemigrations
    python3 manage.py migrate
    python3 manage.py collectstatic
    python3 manage.py test      # Запустите стандартные тесты. Система должна успешна пройти их.
    python3 manage.py createsuperuser       # Создайте суперпользователя.
    python3 manage.py runserver
    
3. Откройте браузер по адресу `http://127.0.0.1:8000/admin/` для перехода в панель администратора сайта.
4. Попробуйте создать несколько тестовых объектов каждого типа.
5. Откройте вкладку `http://127.0.0.1:8000`, чтобы увидеть основной сайт с вашими новыми объектами.