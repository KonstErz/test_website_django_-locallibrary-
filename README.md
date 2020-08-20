# Local Library (Django)

| [Русская версия](https://github.com/KonstErz/test_website_django_-locallibrary-/blob/master/README.ru.md) |

This is a small training website written in Django.
It was created as part of the Django tutorial from [MDN web docs](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django).


## Characteristics

This web application creates an online catalog for a small local library, where users can browse available books and manage their accounts.

The main features that have currently been implemented are:

+ There are models for books, book copies, authors, genres and languages.
+ Users can view a list of books and authors and detailed information about them.
+ Admin users can create and manage models. The admin has been optimised.
+ Librarians (users with Staff status) can update reserved books, as well as create new authors and books, update data about them, or delete them.
+ This website is deployed on a Heroku free server.

## Quick Start

You can run this project locally on your computer by following these steps:

1. Set up the [Python development environment](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/development_environment). It's recommended using a Python virtual environment.  

With python3 on your local machine, you can run this project in a virtual environment by following these steps:  

+ Create a folder for the project named 'test_django_project'. Go to this folder and clone the repository with the project:

    ```
    git clone https://github.com/KonstErz/test_website_django_-locallibrary-.git .
    ```

+ Create a virtual python3 environment in the same folder using the following command:

    ```
    python3 -m venv env
    ```

where *'env'* is the name of the virtual environment.

+ Activate the created virtual environment:

    ```
    source env/bin/activate
    ```

2. After creating and activating the virtual environment from the root directory of the project, run the following commands in the terminal (if you're on Windows you may use `py` or `py -3` instead of `python` to start Python):

    ```
    pip3 install -r requirements.txt
    python3 manage.py makemigrations
    python3 manage.py migrate
    python3 manage.py collectstatic
    python3 manage.py test      # Run the standard tests. These should all pass.
    python3 manage.py createsuperuser       # Create a superuser.
    python3 manage.py runserver
    ```

3. Open a browser to `http://127.0.0.1:8000/admin/` to open the admin panel of the site.
4. Try to create a few test objects of each type.
5. Open tab to `http://127.0.0.1:8000/catalog/` to see the main site, with your new objects.
