# Generated by Django 2.0.1 on 2020-07-27 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsorshiptype',
            name='eng_name',
            field=models.CharField(max_length=30, verbose_name='English type name'),
        ),
    ]
