from django.db import models
from django.conf import settings


class Organization(models.Model):
    """ Organization Model class """
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    admin = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='organization_admin',
        on_delete=models.CASCADE
    )
    people = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='organization_people'
    )


class Workspace(models.Model):
    """ Workspace Model class """
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    organization = models.ForeignKey(
        Organization,
        related_name='workspace_organization',
        on_delete=models.CASCADE
    )
    admin = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='workspace_admin',
        on_delete=models.CASCADE
    )
    people = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='workspace_people',
    )
