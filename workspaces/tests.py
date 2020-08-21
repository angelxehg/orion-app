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

    @staticmethod
    def msg(org_id, chn_id):
        return API.chn(org_id, chn_id) + 'messages/'

    @staticmethod
    def auth(par):
        return '/api/v1/auth/jwt/{}/'.format(par)

    @staticmethod
    def users():
        return '/api/v1/auth/users/'

    @staticmethod
    def search():
        return '/api/v1/search/'


class FunctionalTests(APITestCase):

    def setUp(self):
        self.username = 'functionalman'
        self.password = 'functionalpass'
        self.user = User.objects.create_user(
            username=self.username, password=self.password)
        self.org = models.Organization.objects.create(
            title="Nova X",
            description="Functional organization",
            admin=self.user
        )
        self.wks = models.Workspace.objects.create(
            title="Workspace",
            description="Functional workspace",
            admin=self.user,
            organization=self.org
        )
        self.chn = models.Channel.objects.create(
            title="Channel",
            description="Functional channel",
            admin=self.user,
            organization=self.org
        )
        self.client.force_authenticate(user=self.user)

    def test_f1(self):
        """ PF1: Acceso a plataforma """
        url = API.auth('create')
        response = self.client.options(url, format='json')
        self.assertEqual(response.status_code, 200)

    def test_f2(self):
        """ PF2: Inicio de sesión """
        url = API.auth('create')
        credentials = {
            'username': 'functionalman',
            'password': 'functionalpass'
        }
        response = self.client.post(url, credentials, format='json')
        json_data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertIn('access', json_data)
        self.assertIn('refresh', json_data)

    def test_f3(self):
        """ PF3: Organización """
        url = API.org(self.org.id)
        response = self.client.options(url, format='json')
        json_data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertIn('name', json_data)
        self.assertIn('description', json_data)

    def test_f4(self):
        """ PF4: Mensajes instantáneos """
        url = API.msg(self.org.id, self.chn.id)
        message = {
            'content': 'This is the message content'
        }
        response = self.client.post(url, message, format='json')
        json_data = response.json()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(json_data['content'], message['content'])
        self.assertEqual(json_data['author_name'], 'functionalman')
        self.assertTrue(json_data['mine_flag'])

    def test_f5(self):
        """ PF5: Canales y mensajes """
        url = API.msg(self.org.id, self.chn.id)
        message = {
            'content': 'This is the message in the channel'
        }
        response1 = self.client.post(url, message, format='json')
        response2 = self.client.get(url, message, format='json')
        json_data1 = response1.json()
        json_data2 = response2.json()
        last_msg = json_data2[-1]
        self.assertEqual(response1.status_code, 201)
        self.assertEqual(response2.status_code, 200)
        self.assertEqual(json_data1['content'], message['content'])
        self.assertEqual(json_data1['author_name'], 'functionalman')
        self.assertTrue(json_data1['mine_flag'])
        self.assertGreater(len(json_data2), 0)
        self.assertEqual(last_msg['content'], message['content'])
        self.assertEqual(last_msg['author_name'], 'functionalman')
        self.assertTrue(last_msg['mine_flag'])

    def test_f6(self):
        """ PF6: Búsqueda avanzada """
        url = API.search()
        response = self.client.options(url, format='json')
        self.assertEqual(response.status_code, 200)


class UnitTests(APITestCase):

    def setUp(self):
        self.username = 'testman'
        self.password = 'testpass'
        self.user = User.objects.create_user(
            username=self.username,
            password=self.password)
        self.org = models.Organization.objects.create(
            title="Nova X",
            description="Main organization",
            admin=self.user
        )
        self.wks = models.Workspace.objects.create(
            title="Workspace",
            description="Main workspace",
            admin=self.user,
            organization=self.org
        )
        self.chn = models.Channel.objects.create(
            title="Channel",
            description="Main channel",
            admin=self.user,
            organization=self.org
        )
        self.client.force_authenticate(user=self.user)

    def test_u1_1(self):
        """ PU1.1: API REST """
        url = API.org()
        response = self.client.options(url, format='json')
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
        url = API.users()
        new_user = {
            'username': 'stranger',
            'email': 'stranger@dot.com',
            'password': 'my_fast_pass',
            're_password': 'my_fast_pass'
        }
        response = self.client.post(url, new_user, format='json')
        json_data = response.json()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(json_data['email'], new_user['email'])
        self.assertEqual(json_data['username'], new_user['username'])

    def test_u2_2(self):
        """ PU2.2: Inicio mediante API """
        url = API.auth('create')
        credentials = {
            'username': 'testman',
            'password': 'testpass'
        }
        response = self.client.post(url, credentials, format='json')
        json_data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertIn('access', json_data)
        self.assertIn('refresh', json_data)

    def test_u3_1(self):
        """ PU3.1: Crear organización """
        url = API.org()
        new_org = {
            'title': 'Nova Organization',
            'description': 'We make Nova Software'
        }
        response = self.client.post(url, new_org, format='json')
        json_data = response.json()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(json_data['title'], new_org['title'])
        self.assertEqual(json_data['description'], new_org['description'])
        self.assertTrue(json_data['admin_flag'])
        self.assertEqual(len(json_data['people']), 1)

    def test_u3_2(self):
        """ PU3.2: Obtener organizaciones """
        url = API.org()
        response = self.client.get(url, format='json')
        json_data = response.json()
        self.assertEqual(response.status_code, 200)

    def test_u4_1(self):
        """ PU4.1: Enviar mensaje """
        url = API.msg(self.org.id, self.chn.id)
        message = {
            'content': 'This is the message content'
        }
        response = self.client.post(url, message, format='json')
        json_data = response.json()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(json_data['content'], message['content'])
        self.assertEqual(json_data['author_name'], 'testman')
        self.assertTrue(json_data['mine_flag'])

    def test_u4_2(self):
        """ PU4.2: Recibir mensaje """
        url = API.msg(self.org.id, self.chn.id)
        response = self.client.get(url, format='json')
        json_data = response.json()
        self.assertEqual(response.status_code, 200)

    def test_u5_1(self):
        """ PU5.1: Crear canal """
        url = API.chn(self.org.id)
        new_chn = {
            'title': 'Nova Channel',
            'description': 'Official communications channel'
        }
        response = self.client.post(url, new_chn, format='json')
        json_data = response.json()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(json_data['title'], new_chn['title'])
        self.assertEqual(json_data['description'], new_chn['description'])
        self.assertTrue(json_data['admin_flag'])
        self.assertEqual(len(json_data['people']), 1)

    def test_u5_2(self):
        """ PU5.2: Obtener canales """
        url = API.chn(self.org.id)
        response = self.client.get(url, format='json')
        json_data = response.json()
        self.assertEqual(response.status_code, 200)

    def test_u6(self):
        """ PU6: Búsqueda """
        url = API.search()
        response = self.client.options(url, format='json')
        self.assertEqual(response.status_code, 200)
