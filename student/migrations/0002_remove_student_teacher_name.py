# Generated by Django 5.0.6 on 2024-05-14 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='teacher_name',
        ),
    ]
