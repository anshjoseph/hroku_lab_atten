from django.db import models
# Create your models here.
class day1(models.Model):
    name= models.CharField(max_length=100)
    it = models.BooleanField()
    cs = models.BooleanField()
    def __str__(self):
        return self.name
