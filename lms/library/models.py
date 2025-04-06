from django.db import models

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)  # Название книги
    author = models.CharField(max_length=100)  # Автор
    is_available = models.BooleanField(default=True)  # Доступна ли для выдачи

    def __str__(self):
        return self.title  # Чтобы в админке отображались названия книг
