from djoser.conf import User
from rest_framework import serializers
from workspaces.models import Organization, Workspace


class OrganizationSerializer(serializers.ModelSerializer):
    admin = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    people = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=User.objects.all(),
        required=False
    )

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


class WorkspaceSerializer(serializers.ModelSerializer):
    admin = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    organization = serializers.HiddenField(
        default=1,
    )
    people = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=User.objects.all(),
        required=False
    )

    def create(self, validated_data):
        organization = Organization.objects.get(pk=self.context["view"].kwargs["organization_pk"])
        validated_data["organization"] = organization
        people = []
        if "people" in validated_data:
            people = validated_data["people"]
            del validated_data["people"]
        workspace = Workspace.objects.create(**validated_data)
        for user in people:
            workspace.people.add(user)
        admin = workspace.admin
        if admin not in workspace.people.all():
            workspace.people.add(admin)
        return workspace

    class Meta:
        model = Workspace
        fields = ('id', 'title', 'description', 'organization', 'admin', 'people')
