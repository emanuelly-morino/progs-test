import unittest
from Pessoa import *
from Cliente import *

class TestarPessoa(unittest.TestCase):
    def test_criacao(self):
        obj = Pessoa("João da Silva", "47 9 1234 5678", date(1976, 1, 1))
        obj2 = Cliente(obj, "josilva@gmail.com")
        self.assertEqual(obj2.pessoa.nome, "João da Silva")
        self.assertEqual(obj2.email, "josilva@gmail.com")
