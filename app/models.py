from django.db import models

from django.contrib.auth.models import User
# Create your models here.


class Url(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    longUrl = models.TextField(null=False, blank=False)
    shortUrl = models.CharField(max_length=30)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['create']
