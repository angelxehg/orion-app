from django.db import models

# Create your models here.


class Hero(models.Model):
    """ Example Hero Model """
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)

    def __str__(self):
        """ str(Hero) returns Hero's name """
        return self.name
