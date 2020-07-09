from django.shortcuts import render

from rest_framework import viewsets
from . import models
from . import serializers
from .permissions import IsAdmin


# class OrganizationViewset(viewsets.ModelViewSet):
#     """ Organization Model view set """
#     queryset = models.Organization.objects.all()
#     serializer_class = serializers.OrganizationSerializer
#     permission_classes = [IsAdmin]


# class WorkspaceViewset(viewsets.ModelViewSet):
#     """ Organization Model view set """
#     queryset = models.Workspace.objects.all()
#     serializer_class = serializers.WorkspaceSerializer
#     permission_classes = [IsAdmin]

#     def get_queryset(self):
#         return models.Workspace.objects.filter(parent=self.kwargs['organization_pk'])


# class GroupViewset(viewsets.ModelViewSet):
#     """ Organization Model view set """
#     queryset = models.Group.objects.all()
#     serializer_class = serializers.GroupSerializer

#     def get_queryset(self):
#         return models.Group.objects.filter(parent=self.kwargs['organization_pk'])
