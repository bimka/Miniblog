# Generated by Django 3.2.4 on 2021-12-15 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20211215_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jokes',
            name='joke_rating',
            field=models.IntegerField(default=1),
        ),
    ]
