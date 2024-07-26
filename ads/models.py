from django.db import models
from django.contrib.auth.models import User

class Ad(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)
    position = models.IntegerField()

    class Meta:
        verbose_name = 'ad'
        verbose_name_plural = 'ads'

    def __str__(self):
        return self.title
