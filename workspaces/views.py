from django.shortcuts import render

from rest_framework import viewsets
from . import models
from . import serializers
from .permissions import IsObjectAdmin, IsMessageAuthor


class SearchViewset(viewsets.ReadOnlyModelViewSet):
    """ Search Model view set """
    queryset = models.SearchResult.objects.all()
    serializer_class = serializers.SearchSerializer


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
        return user.organizations.all()


class WorkspaceViewset(viewsets.ModelViewSet):
    """ Workspace Model view set """
    queryset = models.Workspace.objects.all()
    serializer_class = serializers.WorkspaceSerializer
    permission_classes = [IsObjectAdmin]

    def get_queryset(self):
        """
        This view should return a list of all the organizations
        for the currently authenticated user.
        """
        user = self.request.user
        return user.workspaces.filter(organization=self.kwargs['organization_pk'])


class ChannelViewset(viewsets.ModelViewSet):
    """ Channel Model view set """
    queryset = models.Channel.objects.all()
    serializer_class = serializers.ChannelSerializer
    permission_classes = [IsObjectAdmin]

    def get_queryset(self):
        """
        This view should return a list of all the organizations
        for the currently authenticated user.
        """
        user = self.request.user
        return user.channels.filter(organization=self.kwargs['organization_pk'])


class MessageViewset(viewsets.ModelViewSet):
    """ Message Model view set """
    queryset = models.Message.objects.all()
    serializer_class = serializers.MessageSerializer
    permission_classes = [IsMessageAuthor]

    def get_queryset(self):
        """
        This view should return a list of all the organizations
        for the currently authenticated user.
        """
        return models.Message.objects.filter(channel=self.kwargs['channel_pk'])
