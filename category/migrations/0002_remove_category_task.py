# Generated by Django 5.0.3 on 2024-03-27 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='task',
        ),
    ]
