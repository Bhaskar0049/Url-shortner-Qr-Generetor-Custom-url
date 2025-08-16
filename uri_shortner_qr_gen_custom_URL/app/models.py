from django.db import models

# Create your models here.
from django.db import models

class URL(models.Model):
    original_url = models.URLField()
    short_url = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.original_url

class Custom_url(models.Model):
    original_url =models.URLField()
    custom_url=models.CharField(max_length=100)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.original_url