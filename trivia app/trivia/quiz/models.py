from django.db import models
from django.db.models.fields import CharField


# Create your models here.
class Name(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return "{}".format(self.name)


