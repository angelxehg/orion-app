from django.db import models
from django.conf import settings


class Organization(models.Model):
    """ Organization Model class """
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    people = models.ManyToManyField(
        settings.AUTH_USER_MODEL
    )


# class Organization(BasicModel):
#     """ Organization Model class """
#     people = models.OneToOneField(
#         Placeholder,
#         on_delete=models.CASCADE
#     )


# class OrganizationChild(models.Model):
#     """ Organization Child Model abstract class """
#     parent = models.ForeignKey(
#         Organization,
#         on_delete=models.CASCADE
#     )

#     class Meta:
#         abstract = True


# class Placeholder(BasicModel):
#     """ User Placeholder Model class """
#     users = models.ManyToManyField(
#         settings.AUTH_USER_MODEL,
#     )


# class Group(BasicModel, OrganizationChild):
#     """ Group Model class """
#     default = models.BooleanField()


# class Workspace(BasicModel, OrganizationChild):
#     """ Workspace Model class """
#     default = models.BooleanField()


# class Group(OrganizationChild):
#     """ Group Model class """
#     title = models.CharField(max_length=50)
#     description = models.CharField(max_length=1000)
#     users = models.ManyToManyField(
#         settings.AUTH_USER_MODEL,
#     )


# class Workspace(ManagedModel, OrganizationChild):
#     """ Workspace Model class """
#     title = models.CharField(max_length=50)
#     description = models.CharField(max_length=1000)
#     groups = models.ManyToManyField(
#         Group,
#     )
