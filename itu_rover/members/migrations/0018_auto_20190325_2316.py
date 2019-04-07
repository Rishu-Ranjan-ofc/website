# Generated by Django 2.0.1 on 2019-03-25 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0017_auto_20190325_2303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subteam',
            name='leader',
        ),
        migrations.AddField(
            model_name='subteam',
            name='leaders',
            field=models.ManyToManyField(blank=True, null=True, related_name='leader_of', to='members.Member', verbose_name='subteam leader'),
        ),
    ]