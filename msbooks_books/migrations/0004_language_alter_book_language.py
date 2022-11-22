# Generated by Django 4.1.3 on 2022-11-22 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('msbooks_books', '0003_genre_book_language_book_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name': 'язык',
                'verbose_name_plural': 'языки',
            },
        ),
        migrations.AlterField(
            model_name='book',
            name='language',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='msbooks_books.language'),
        ),
    ]
