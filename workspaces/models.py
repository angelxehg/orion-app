from django.db import models
from django.conf import settings


class Organization(models.Model):
    """ Organization Model class """
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    admin = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='admin_organizations',
        on_delete=models.CASCADE
    )
    people = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='organizations'
    )

    objects = models.Manager()


class Workspace(models.Model):
    """ Workspace Model class """
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    organization = models.ForeignKey(
        Organization,
        related_name='workspaces',
        on_delete=models.CASCADE
    )
    admin = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='admin_workspaces',
        on_delete=models.CASCADE
    )
    people = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='workspaces',
    )

    objects = models.Manager()


class Channel(models.Model):
    """ Channel Model class """
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    organization = models.ForeignKey(
        Organization,
        related_name='channels',
        on_delete=models.CASCADE
    )
    admin = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='admin_channels',
        on_delete=models.CASCADE
    )
    people = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='channels',
    )

    objects = models.Manager()
