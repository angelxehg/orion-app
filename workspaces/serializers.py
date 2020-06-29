from rest_framework import serializers
from . import models


class OrganizationSerializer(serializers.ModelSerializer):
    admin = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = models.Organization
        fields = ('id', 'title', 'description', 'admin')
