# Generated by Django 2.0.1 on 2020-01-10 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oldyears', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oldyear',
            name='year',
            field=models.CharField(max_length=2, unique=True, verbose_name='team year'),
        ),
    ]