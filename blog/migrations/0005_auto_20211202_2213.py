# Generated by Django 3.2.4 on 2021-12-02 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_jokes_joke_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jokes',
            name='joke_rating',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='jokes',
            name='joke_text',
            field=models.TextField(max_length=500, verbose_name='Текст шутки'),
        ),
    ]