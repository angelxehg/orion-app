from rest_framework import serializers
from . import models


class OrganizationSerializer(serializers.ModelSerializer):
    """ Organization Model serializer """
    class Meta:
        model = models.Organization
        fields = ('id', 'title', 'description')
