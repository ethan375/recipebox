# Generated by Django 2.2.7 on 2019-11-19 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_author_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='password',
        ),
    ]
