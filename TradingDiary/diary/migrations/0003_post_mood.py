# Generated by Django 3.1.4 on 2021-01-21 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0002_remove_post_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='mood',
            field=models.CharField(choices=[('EP', 'Epic'), ('GR', 'Great'), ('NE', 'Neutral'), ('BA', 'Bad'), ('PA', 'Pathetic')], default='NE', max_length=2),
        ),
    ]
