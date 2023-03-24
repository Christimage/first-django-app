# Generated by Django 4.1.7 on 2023-03-08 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfirstapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='details',
            field=models.CharField(default='Details', max_length=500),
        ),
        migrations.AddField(
            model_name='item',
            name='img_url',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='name',
            field=models.CharField(default='Item', max_length=50, unique=True),
        ),
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.FloatField(default=0.0, max_length=5),
        ),
    ]