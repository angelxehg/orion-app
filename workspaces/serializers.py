from djoser.conf import User
from rest_framework import serializers
from workspaces.models import Organization


class OrganizationSerializer(serializers.ModelSerializer):
    admin = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    people = serializers.PrimaryKeyRelatedField(
        many=True, queryset=User.objects.all(), required=False)

    def create(self, validated_data):
        people = []
        if "people" in validated_data:
            people = validated_data["people"]
            del validated_data["people"]
        organization = Organization.objects.create(**validated_data)
        for user in people:
            organization.people.add(user)
        admin = organization.admin
        if admin not in organization.people.all():
            organization.people.add(admin)
        return organization

    class Meta:
        model = Organization
        fields = ('id', 'title', 'description', 'admin', 'people')
