from django.db import models
from datetime import datetime

# Create your models here.
class Image(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='images/')
    result = models.CharField(max_length=100, default='')
    date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.id

