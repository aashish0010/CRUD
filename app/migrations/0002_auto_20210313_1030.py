# Generated by Django 3.1.7 on 2021-03-13 04:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='crud',
            old_name='name',
            new_name='username',
        ),
    ]