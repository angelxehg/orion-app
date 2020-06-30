from djoser.conf import User
from rest_framework import serializers
from . import models


class OrganizationSerializer(serializers.ModelSerializer):
    admin = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = models.Organization
        fields = ('id', 'title', 'description', 'admin')


class WorkspaceSerializer(serializers.ModelSerializer):
    admin = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    parent = serializers.HiddenField(
        default=3,
    )

    def create(self, validated_data):
        parent = models.Organization.objects.get(pk=self.context["view"].kwargs["organization_pk"])
        validated_data["parent"] = parent
        return models.Workspace.objects.create(**validated_data)

    class Meta:
        model = models.Workspace
        fields = ('id', 'title', 'description', 'admin', 'parent')


class GroupSerializer(serializers.ModelSerializer):
    parent = serializers.HiddenField(
        default=3,
    )
    users = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all(), required=False)

    def create(self, validated_data):
        parent = models.Organization.objects.get(pk=self.context["view"].kwargs["organization_pk"])
        validated_data["parent"] = parent
        users = validated_data["users"]
        del validated_data["users"]
        group = models.Group.objects.create(**validated_data)
        for user in users:
            group.users.add(user)
        return group

    class Meta:
        model = models.Group
        fields = ('id', 'title', 'description', 'parent', 'users')
