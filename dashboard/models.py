from django.db import models
from django.forms import ModelForm

# Create your models here.
class Dashes(models.Model):
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=10000, default='', verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deadline_at = models.DateTimeField(verbose_name='Дата окончания')
    views_count = models.IntegerField(verbose_name='Количество просмотров', default=0)

    def __str__(self):
        return self.title
    def incrementViewsCount(self):
        self.views_count +=1
        self.save()