from django.db import models
from django.urls import reverse

# Create your models here.

class Widget(models.Model):
    description = models.CharField(max_length=50)
    quantitiy = models.IntegerField(max_length=10)

    def __str__(self):
        return self.
    
    def get_absolute_url(self):
        return reverse('index')