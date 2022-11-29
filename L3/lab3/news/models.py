from django.db import models

class News(models.Model):
    title = models.CharField(verbose_name=u'Заголовок', max_length=255)
    text = models.CharField(verbose_name=u'Текст статті', max_length=255)
    def __str__(self):
        return f"{self.id}: {self.title} : {self.text}"