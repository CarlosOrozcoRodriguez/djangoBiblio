from django.db import models

# Create your models here.
class Book(models.Model):
    user_id = models.IntegerField()
    title = models.CharField(max_length = 255)
    author = models.CharField(max_length = 255)
    genre = models.CharField(max_length = 255)
    publisher = models.CharField(max_length = 255)
    year = models.IntegerField()

class Loan (models.Model):
    user_id = models.IntegerField()
    book_id = models.IntegerField()
    loan_date = models.DateField()
    due_date = models.DateField()

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    address = models.CharField(max_length = 255)
    phone = models.CharField(max_length = 20)
    email = models.EmailField()