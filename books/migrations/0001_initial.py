# Generated by Django 5.0.6 on 2024-06-02 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostBooks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Напишите название книги')),
                ('image', models.ImageField(blank=True, upload_to='images/', verbose_name='Загрузите фото')),
                ('description', models.TextField(verbose_name='Напишите аннотацию к книге')),
                ('music', models.FileField(blank=True, upload_to='audio/', verbose_name='Загрузите песню')),
                ('video', models.URLField(blank=True, verbose_name='укажите видео ссылку')),
                ('category', models.CharField(choices=[('Классика', 'Классика'), ('Совеременное', 'Совеременное'), ('Ужасы', 'Ужасы'), ('Комедия', 'Комедия'), ('Философия', 'Философия'), ('Научпоп', 'Научпоп'), ('Фантастика', 'Фантастика')], max_length=100, verbose_name='выберите категорию')),
                ('cost_list', models.PositiveIntegerField(blank=True, verbose_name='Укажите количество страниц')),
                ('author', models.CharField(max_length=100, verbose_name='Укажите автора')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('genres', models.CharField(choices=[('Роман', 'Роман'), ('Повесть', 'Повесть'), ('Рассказ', 'Рассказ'), ('Новелла', 'Новелла'), ('Пьеса', 'Пьеса'), ('Эпопея', 'Эпопея'), ('Поэма', 'Поэма')], max_length=1000, verbose_name='выберите жанр')),
            ],
            options={
                'verbose_name': 'книгу',
                'verbose_name_plural': 'список книг',
            },
        ),
    ]
