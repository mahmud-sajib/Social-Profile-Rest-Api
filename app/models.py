from django.db import models
from django.conf import settings

# Create your models here.

class Status(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    image = models.FileField(upload_to='uploads/%Y/%m/%d', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.author)

    class Meta:
        verbose_name_plural = "Author Status"
