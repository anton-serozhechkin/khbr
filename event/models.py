from django.db import models
from django.urls import reverse
from django.utils import timezone
from analytics.models import Author

class Event(models.Model):
    title = models.CharField('Заголовок',max_length=120)
    slug = models.SlugField('Ссылка')
    short_description = models.CharField('Короткое описание на 200 символов', max_length=200)
    day = models.DateField('День события')
    start_time = models.TimeField('Начало', blank=True)
    end_time = models.TimeField('Конец', blank=True)
    place = models.CharField('Место', blank=True, max_length=300)
    image = models.ImageField('Фотография', blank=True)
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING, verbose_name="Автор")
    content = models.TextField('Контент', blank=True, null=True)
    created = models.DateTimeField('Дата создания', default=timezone.now)
    is_active = models.BooleanField(default=True, verbose_name='Видимость для пользователя')
    
    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('event_detail', kwargs={'slug': self.slug})