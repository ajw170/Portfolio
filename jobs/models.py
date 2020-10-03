from django.db import models

# Create your models here.
class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    short_summary = models.CharField(max_length=50,default='Add Summary Here',name='Short Summary')


    def __str__(self):
        return self.summary