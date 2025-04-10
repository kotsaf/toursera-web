from django.db import models
from django.utils import timezone

class Tours(models.Model):
    name = models.CharField('Название тура',max_length=60, blank=False)
    description = models.TextField('О туре', max_length=500, blank=False)
    price = models.IntegerField('Цена', default=0, blank=False)

    def __str__(self):
        return f'{self.id} - {self.name}'

    class Meta:
        verbose_name = 'Тур'
        verbose_name_plural = 'Туры'

class Feedback(models.Model):
    feedbacker = models.CharField('Ваше имя', max_length=50, blank=False)
    title = models.CharField('Превью отзыва', max_length=50, blank=False)
    feedback = models.TextField('Отзыв', max_length=800)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f'Отзыв от {self.feedbacker}'
    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'