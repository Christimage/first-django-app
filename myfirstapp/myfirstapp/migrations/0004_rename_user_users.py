# Generated by Django 4.1.7 on 2023-03-10 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myfirstapp', '0003_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Users',
        ),
    ]