# Generated by Django 3.1.4 on 2021-01-07 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0002_auto_20210106_2101'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='result',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]