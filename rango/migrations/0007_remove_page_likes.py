# Generated by Django 3.0 on 2020-01-29 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0006_page_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='likes',
        ),
    ]
