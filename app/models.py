from django.db import models

from django.contrib.auth.models import User
# Create your models here.


class Url(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    longUrl = models.TextField(null=False, blank=False)
    shortUrl = models.CharField(max_length=30, primary_key=True)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.shortUrl

    class Meta:
        ordering = ['create']
