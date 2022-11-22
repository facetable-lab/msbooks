# Generated by Django 4.1.3 on 2022-11-22 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msbooks_books', '0002_author_book_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'жанр',
                'verbose_name_plural': 'жанры',
            },
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.CharField(blank=True, default=None, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='year',
            field=models.CharField(blank=True, default=None, max_length=32, null=True),
        ),
    ]
