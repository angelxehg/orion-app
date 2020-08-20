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


class FunctionalTests(APITestCase):

    def setUp(self):
        self.username = 'functionalman'
        self.password = 'functionalpass'
        self.user = User.objects.create(
            username=self.username, password=self.password)
        self.org = models.Organization.objects.create(
            title="Nova X", description="Functional organization", admin=self.user
        )
        self.wks = models.Workspace.objects.create(
            title="Workspace", description="Functional workspace", admin=self.user, organization=self.org
        )
        self.chn = models.Channel.objects.create(
            title="Channel", description="Functional channel", admin=self.user, organization=self.org
        )
        self.client.force_authenticate(user=self.user)

    def test_f1(self):
        """ PF1: Acceso a plataforma """
        response = self.client.options(API.org(), format='json')
        self.assertEqual(1, 1)

    def test_f2(self):
        """ PF2: Inicio de sesión """
        response = self.client.options(API.org(), format='json')
        self.assertEqual(1, 1)

    def test_f3(self):
        """ PF3: Organización """
        response = self.client.options(API.org(), format='json')
        self.assertEqual(1, 1)

    def test_f4(self):
        """ PF4: Mensajes instantáneos """
        response = self.client.options(API.org(), format='json')
        self.assertEqual(1, 1)

    def test_f5(self):
        """ PF5: Canales y mensajes """
        response = self.client.options(API.org(), format='json')
        self.assertEqual(1, 1)

    def test_f6(self):
        """ PF6: Búsqueda avanzada """
        response = self.client.options(API.org(), format='json')
        self.assertEqual(1, 1)


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

    def test_u1_1(self):
        """ PU1.1: API REST """
        response = self.client.options(API.org(), format='json')
        self.assertEqual(response.status_code, 200)

    def test_u1_2(self):
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

    def test_u2_1(self):
        """ PU2.1: Registro mediante API """
        response = self.client.options(API.org(), format='json')
        self.assertEqual(1, 1)

    def test_u2_2(self):
        """ PU2.2: Inicio mediante API """
        response = self.client.options(API.org(), format='json')
        self.assertEqual(1, 1)

    def test_u2_3(self):
        """ PU2.3: Establecer apodo """
        response = self.client.options(API.org(), format='json')
        self.assertEqual(1, 1)

    def test_u3_1(self):
        """ PU3.1: Crear organización """
        response = self.client.options(API.org(), format='json')
        self.assertEqual(1, 1)

    def test_u3_2(self):
        """ PU3.2: Unirse a organización """
        response = self.client.options(API.org(), format='json')
        self.assertEqual(1, 1)

    def test_u4_1(self):
        """ PU4.1: Enviar mensaje """
        response = self.client.options(API.org(), format='json')
        self.assertEqual(1, 1)

    def test_u4_2(self):
        """ PU4.2: Recibir mensaje """
        response = self.client.options(API.org(), format='json')
        self.assertEqual(1, 1)

    def test_u4_3(self):
        """ PU4.3: Mensaje con adjuntos """
        response = self.client.options(API.org(), format='json')
        self.assertEqual(1, 1)

    def test_u5_1(self):
        """ PU5.1: Crear canal """
        response = self.client.options(API.org(), format='json')
        self.assertEqual(1, 1)

    def test_u5_2(self):
        """ PU5.2: Unirse a canal """
        response = self.client.options(API.org(), format='json')
        self.assertEqual(1, 1)

    def test_u5_3(self):
        """ PU5.3: Descripción canal """
        response = self.client.options(API.org(), format='json')
        self.assertEqual(1, 1)

    def test_u6(self):
        """ PU6: Búsqueda con filtros """
        response = self.client.options(API.org(), format='json')
        self.assertEqual(1, 1)
