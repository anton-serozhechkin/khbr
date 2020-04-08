from django.db import models
from django.urls import reverse
from django.utils import timezone
from analytics.models import Author


class Raiting(models.Model):
    title = models.CharField('Заголовок',max_length=200)
    slug = models.SlugField('Ссылка')
    short_description = models.CharField('Короткое описание на 200 символов', max_length=200)
    content = models.TextField('Контент')
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING, verbose_name="Автор")
    image = models.ImageField('Фотография', blank=True)
    created = models.DateTimeField('Дата создания', default=timezone.now)
    is_active = models.BooleanField(default=True, verbose_name='Видимость для пользователя')

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('raiting_detail', kwargs={'slug': self.slug})