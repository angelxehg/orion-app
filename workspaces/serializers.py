from djoser.conf import User
from rest_framework import serializers
from . import models
from .models import Group


# class OrganizationSerializer(serializers.ModelSerializer):
#     admin = serializers.HiddenField(
#         default=serializers.CurrentUserDefault()
#     )

#     class Meta:
#         model = models.Organization
#         fields = ('id', 'title', 'description', 'admin')


# class GroupSerializer(serializers.ModelSerializer):
#     parent = serializers.HiddenField(
#         default=3,
#     )
#     users = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all(), required=False)

#     def create(self, validated_data):
#         parent = models.Organization.objects.get(pk=self.context["view"].kwargs["organization_pk"])
#         validated_data["parent"] = parent
#         users = validated_data["users"]
#         del validated_data["users"]
#         group = models.Group.objects.create(**validated_data)
#         for user in users:
#             group.users.add(user)
#         return group

#     class Meta:
#         model = models.Group
#         fields = ('id', 'title', 'description', 'parent', 'users')


# class WorkspaceSerializer(serializers.ModelSerializer):
#     admin = serializers.HiddenField(
#         default=serializers.CurrentUserDefault()
#     )
#     parent = serializers.HiddenField(
#         default=3,
#     )
#     groups = serializers.PrimaryKeyRelatedField(many=True, queryset=Group.objects.all(), required=False)

#     def create(self, validated_data):
#         parent = models.Organization.objects.get(pk=self.context["view"].kwargs["organization_pk"])
#         validated_data["parent"] = parent
#         groups = validated_data["groups"]
#         del validated_data["groups"]
#         workspace = models.Workspace.objects.create(**validated_data)
#         for group in groups:
#             workspace.groups.add(group)
#         return workspace

#     class Meta:
#         model = models.Workspace
#         fields = ('id', 'title', 'description', 'admin', 'parent', 'groups')
