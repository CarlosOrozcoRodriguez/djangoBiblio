# djangoBiblio

python -m venv djangoenv
djangoenv/Scripts/activate
pip install django
django-admin startproject DBBiblio .
django-admin startapp loans
# agregar la aplicacion loans a settings.py
python manage.py runserver

# creado el modelo de la DB en models.py
# parar el servidor, migrar y crear las tablas en la DB
python manage.py makemigrations

python manage.py migrate