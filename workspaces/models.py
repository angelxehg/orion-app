from django.db import models
from django.conf import settings


class ManagedModel(models.Model):
    """ Managed Model abstract class """
    admin = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    class Meta:
        abstract = True


class Organization(ManagedModel):
    """ Organization Model class """
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
