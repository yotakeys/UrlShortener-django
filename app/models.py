from django.db import models

from django.contrib.auth.models import User
# Create your models here.


class Url(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    oldUrl = models.TextField(null=False, blank=False),
    newUrl = models.TextField(),
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.newUrl

    class Meta:
        ordering = ['create']
