import uuid
from django.db import models

class Document1(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    title = models.CharField('Название', max_length=100, default=uuid.uuid4)
    file = models.FileField()


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'



