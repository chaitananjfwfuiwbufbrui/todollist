from django.db import models

# Create your models here.


class Home(models.Model):
    title = models.CharField(max_length=30)
    desc = models.CharField(max_length=200)
    def __str__ (self):
        return self.title , self.desc