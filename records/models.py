from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Record(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    country=models.CharField(max_length=50)
    date_created=models.DateTimeField(default=timezone.now)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

