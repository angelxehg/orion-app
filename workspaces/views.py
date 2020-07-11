from django.shortcuts import render

from rest_framework import viewsets
from . import models
from . import serializers
from .permissions import IsObjectAdmin


class OrganizationViewset(viewsets.ModelViewSet):
    """ Organization Model view set """
    queryset = models.Organization.objects.all()
    serializer_class = serializers.OrganizationSerializer
    permission_classes = [IsObjectAdmin]

    def get_queryset(self):
        """
        This view should return a list of all the organizations
        for the currently authenticated user.
        """
        user = self.request.user
        return user.organization_set.all()
