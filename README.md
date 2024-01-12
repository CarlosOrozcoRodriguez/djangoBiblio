# djangoBiblio

python -m venv djangoenv
djangoenv/Scripts/activate
pip install django
django-admin startproject DBBiblio .
django-admin startapp loans
# agregar la aplicacion loans a settings.py
#    linea 40 de DBBilio/settings.py
python manage.py runserver

# creado el modelo de la DB en models.py
#    fichero loans/models.py
# parar el servidor, migrar y crear las tablas en la DB //no es necesario parar el servidor
python manage.py makemigrations
python manage.py migrate

# insertar datos a traves de shell
python .\manage.py shell
# >>>
    from biblio.models import Book

    book1 = Book(title='El gran Gatsby', author='F. Scott Fitzgerald', genre='Ficción', year=1925, publisher='Scribner')
    book1.save()