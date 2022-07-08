from django.test import TestCase
from aluraflix.models import Programa

class FixturesDataTestCase(TestCase):
    
    fixtures = ['programas_iniciais']

    def test_verifica_carregamento_da_fixture(self):
        progrma_bizaro = Programa.objects.get(pk=1)
        all_programs = Programa.objects.all()
        self.assertEqual(progrma_bizaro.titulo, 'Coisas bizarras')
        self.assertEqual(len(all_programs), 9)



