# Generated by Django 5.0.1 on 2024-01-12 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='user_id',
        ),
    ]
