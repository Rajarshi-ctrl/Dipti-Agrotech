from django.db import models
import datetime


# Create your models here.
class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=40)
    message = models.CharField(max_length=200)
    date = models.DateTimeField(default=datetime.datetime.now, blank=True,null=True)
    
    def __str__(self):
        return self.name
