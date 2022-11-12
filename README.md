# question-generation-api

make sure to use a virtual env
you must pip install django

This is what is installed in my venv:
I only had to use pip install for `Django` and `djangorestframework`
which you should be able to install using:
`pip install -r requiremennts.txt`
asgiref           3.5.2
Django            3.2.16
djangorestframework 3.14.0
pip               22.1
pytz              2022.6
setuptools        62.2.0
sqlparse          0.4.3
typing_extensions 4.4.0
wheel             0.37.1

You may have to run migrations with `python manage.py migrate`

If you make amy change to the model for 'Questions' or add ny additional models, you will have to run `python manage.py makemigrations` then migrate them with the cmmand above.

#Create a Super User for the admin/db interfaces
`python manage.py createsuperuser`

#Go here to see admin and db data after you run:
`python manage.py runserver`
http://127.0.0.1:8000/admin/

Check out the API Here:
http://127.0.0.1:8000/questions/
if your server is up and running this should take you to an API Root page