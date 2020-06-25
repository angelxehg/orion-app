from django.db import models


class Organization(models.Model):
    """ Organization Model class """
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
