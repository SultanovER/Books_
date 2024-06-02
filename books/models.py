from django.db import models

class PostBooks(models.Model):
    CATEGORY_BOOKS = (
        ('Классика', 'Классика'),
        ('Совеременное', 'Совеременное'),
        ('Ужасы', 'Ужасы'),
        ('Комедия', 'Комедия'),
        ('Философия', 'Философия'),
        ('Научпоп', 'Научпоп'),
        ('Фантастика', 'Фантастика')
    )
    GENRE_BOOKS = (
        ('Роман', 'Роман'),
        ('Повесть', 'Повесть'),
        ('Рассказ', 'Рассказ'),
        ('Новелла', 'Новелла'),
        ('Пьеса', 'Пьеса'),
        ('Эпопея', 'Эпопея'),
        ('Поэма', 'Поэма')
    )

    title = models.CharField(max_length=100, verbose_name='Напишите название книги')
    image = models.ImageField(upload_to='images/', verbose_name='Загрузите фото', blank=True)
    description = models.TextField(verbose_name='Напишите аннотацию к книге')
    music = models.FileField(upload_to='audio/', verbose_name='Загрузите песню', blank=True)
    video = models.URLField(verbose_name='укажите видео ссылку', blank=True)
    category = models.CharField(max_length=100, choices=CATEGORY_BOOKS, verbose_name='выберите категорию')
    cost_list = models.PositiveIntegerField(verbose_name='Укажите количество страниц', blank=True, null=True)
    author = models.CharField(max_length=100, verbose_name='Укажите автора')
    created_at = models.DateTimeField(auto_now_add=True)
    genres = models.CharField(max_length=1000, choices=GENRE_BOOKS, verbose_name='выберите жанр')

    def __str__(self):
        return f"{self.title} - {self.created_at}"
    
    class Meta:
        verbose_name = 'книгу'
        verbose_name_plural = 'список книг'