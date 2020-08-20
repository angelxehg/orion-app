from django.test import TestCase
from django.contrib.auth.models import User
from workspaces import models
from rest_framework.test import APITestCase


class API():
    @staticmethod
    def org(org_id=None):
        if org_id is None:
            return '/api/v1/organizations/'
        return '/api/v1/organizations/{}/'.format(org_id)

    @staticmethod
    def wks(org_id, wks_id=None):
        if wks_id is None:
            return API.org(org_id) + 'workspaces/'
        return API.org(org_id) + 'workspaces/{}/'.format(wks_id)

    @staticmethod
    def chn(org_id, chn_id=None):
        if chn_id is None:
            return API.org(org_id) + 'channels/'
        return API.org(org_id) + 'channels/{}/'.format(chn_id)


class UnitTests(APITestCase):
    def setUp(self):
        self.username = 'testman'
        self.password = 'testpass'
        self.user = User.objects.create(
            username=self.username, password=self.password)
        self.org = models.Organization.objects.create(
            title="Nova X", description="Main organization", admin=self.user
        )
        self.wks = models.Workspace.objects.create(
            title="Workspace", description="Main workspace", admin=self.user, organization=self.org
        )
        self.chn = models.Channel.objects.create(
            title="Channel", description="Main channel", admin=self.user, organization=self.org
        )
        self.client.force_authenticate(user=self.user)

    def test_u1_1_api_rest(self):
        """ PU1.1: API REST """
        response = self.client.options(API.org(), format='json')
        self.assertEqual(response.status_code, 200)

    def test_u1_2_services(self):
        """ PU1.2: Microservices """
        org_url = API.org(self.org.id)
        wks_url = API.wks(self.org.id, self.wks.id)
        chn_url = API.chn(self.org.id, self.wks.id)
        org_options = self.client.options(org_url, format='json')
        wks_options = self.client.options(wks_url, format='json')
        chn_options = self.client.options(chn_url, format='json')
        self.assertEqual(org_options.status_code, 200)
        self.assertEqual(wks_options.status_code, 200)
        self.assertEqual(chn_options.status_code, 200)
