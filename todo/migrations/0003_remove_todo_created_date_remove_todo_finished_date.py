# Generated by Django 4.1.2 on 2022-10-20 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todo_created_date_todo_finished_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='finished_date',
        ),
    ]
