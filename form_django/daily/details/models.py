from django.db import models

# Create your models here.


class Details(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField(max_length=120)
    password = models.CharField(max_length=64)

    def __str__(self) :
        return self.name