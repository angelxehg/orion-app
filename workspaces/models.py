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


class OrganizationChild(models.Model):
    """ Organization Child Model abstract class """
    parent = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE
    )

    class Meta:
        abstract = True


class Group(OrganizationChild):
    """ Group Model class """
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
    )


class Workspace(ManagedModel, OrganizationChild):
    """ Workspace Model class """
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    groups = models.ManyToManyField(
        Group,
    )
