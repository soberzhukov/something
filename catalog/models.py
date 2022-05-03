import uuid

from django.db import models
from django.urls import reverse


class Genre(models.Model):
    """
    Жанр книги
    """
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    name = models.CharField('Название жанра', max_length=200, help_text='Введите жанр книги')

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Книга
    """
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    title = models.CharField('Название', max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True, related_name='books')
    summary = models.TextField('Краткое описание', max_length=1000, help_text="Введите краткое описание")
    isbn = models.CharField('ISBN', max_length=13)
    genre = models.ManyToManyField(Genre, help_text="Выберите жанр для этой книги", related_name='books')

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])


class StatusBookInstance:
    MAINTENANCE = 'm'
    ON_LOAN = 'o'
    AVAILABLE = 'a'
    RESERVED = 'r'


class BookInstance(models.Model):
    """
    Экземпляр книги
    """
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    due_back = models.DateField('Когда будет доступна', null=True, blank=True)
    STATUS_CHOICES = (
        (StatusBookInstance.MAINTENANCE, 'Техническое обслуживание'),
        (StatusBookInstance.ON_LOAN, 'В аренде'),
        (StatusBookInstance.AVAILABLE, 'Доступно'),
        (StatusBookInstance.RESERVED, 'Зарезервировано'),
    )
    status = models.CharField('Статус', max_length=1, choices=STATUS_CHOICES, blank=True,
                              default=StatusBookInstance.MAINTENANCE)

    class Meta:
        ordering = ["due_back"]
        verbose_name = 'Экземпляр'
        verbose_name_plural = 'Экземпляры'

    def __str__(self):
        return f'{self.id}, {self.book.title}'


class Author(models.Model):
    """
    Автор
    """
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField('Имя', max_length=100)
    last_name = models.CharField('Фамилия', max_length=100)
    date_of_birth = models.DateField('Дата рождения', null=True, blank=True)
    date_of_death = models.DateField('Дата смерти', null=True, blank=True)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])