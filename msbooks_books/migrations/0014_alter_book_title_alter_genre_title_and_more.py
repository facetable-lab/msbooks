# Generated by Django 4.1.3 on 2022-11-22 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msbooks_books', '0013_alter_genre_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='genre',
            name='title',
            field=models.CharField(max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='language',
            name='title',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]