from django.test import TestCase
from rest_framework.test import APIClient

class teste(TestCase):

    @classmethod
    def setUp(cls):
        super(teste, cls)
        cls.client = APIClient()

# Teste get
    def test_register1(self):
        response = self.client.get('/usuarios')
        assert response.status_code == 200

# Teste post
    def test_register2(self):
        data = {
            "nome": "teste",
            "email": "teste@teste.com",   
            "senha": "teste123",
            "tipo": 1,
        }
        response = self.client.post('/usuarios', data)
        assert response.status_code == 201

# Teste caso o email nao estiver no formato correto
    def test_register3(self):
        data = {
            "nome": "teste",
            "email": "teste",
            "senha": "teste123",
            "tipo": 1,
        }
        response = self.client.post('/usuarios', data)
        assert response.status_code == 400

# Teste caso o email estiver vazio
    def test_register4(self):
        data = {
            "nome": "teste",
            "email": " ",
            "senha": "teste123",
            "tipo": 1,
        }
        response = self.client.post('/usuarios', data)
        assert response.status_code == 400

# Teste caso o nome estiver vazio
    def test_register5(self):
        data = {
            "nome": " ",
            "email": "teste@teste.com",
            "senha": "teste123",
            "tipo": 1,
        }
        response = self.client.post('/usuarios', data)
        assert response.status_code == 400

# Teste caso senha estiver vazia
    def test_register6(self):
        data = {
            "nome": "teste",
            "email": "teste@teste.com",
            "senha": " ",
            "tipo": 1,
        }
        response = self.client.post('/usuarios', data)
        assert response.status_code == 400

