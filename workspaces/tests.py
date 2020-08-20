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
            return API.org(org_id) + '/workspaces/'
        return API.org(org_id) + '/workspaces/{}/'.format(wks_id)


class UnitTests(APITestCase):
    def setUp(self):
        self.username = 'testman'
        self.password = 'testpass'
        self.user = User.objects.create(
            username=self.username, password=self.password)
        self.client.force_authenticate(user=self.user)

    def test_u1_1_api_rest(self):
        """ PU1.1: API REST """
        response = self.client.options(API.org(), format='json')
        self.assertEqual(response.status_code, 200)
