from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Topic(models.Model):
    name = models.CharField(max_length=255)     

class News(models.Model):
    title = models.CharField(verbose_name=u'Заголовок', max_length=255)
    text = models.CharField(verbose_name=u'Текст статті', max_length=255)
    topic = models.ForeignKey(Topic, null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.topic.name}"