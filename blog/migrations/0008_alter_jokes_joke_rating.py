# Generated by Django 3.2.4 on 2021-12-07 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_jokes_joke_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jokes',
            name='joke_rating',
            field=models.IntegerField(default=9),
        ),
    ]
