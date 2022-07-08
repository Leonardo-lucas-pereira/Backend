from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status

class AuthenticationUserTestCase(APITestCase):
    
    def setUp(self):
        self.list_url = reverse('programas-list')
        self.user = User.objects.create_user('c3po', password='123456')

    def test_autenticacao_user_credenciais_corretas(self):
        """Teste que verifica a autenticação de user com as credencias corretas"""
        user = authenticate(username='c3po', password='123456')
        self.assertTrue((user is not None)and user.is_authenticated)

    def test_requisicao_get_nao_autoriizada(self):
        """Teste que verifica uma requisição GET não autorizada"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)


    def test_autenticacao_de_username_incorreto(self):
        """Verificando user com username incorreto"""
        user = authenticate(username='c3pp', password='123456')
        self.assertFalse((user is not None)and user.is_authenticated)

    def test_autenticacao_de_password_incorreto(self):
        """Verificando user com password incorreto"""
        user = authenticate(username='c3po', password='123')
        self.assertFalse((user is not None)and user.is_authenticated)
