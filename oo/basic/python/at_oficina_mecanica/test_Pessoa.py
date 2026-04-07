import unittest
from Pessoa import *

class TestarPessoa(unittest.TestCase):
    def test_criacao(self):
        obj = Pessoa("João da Silva", "47 9 1234 5678", date(1976, 1, 1))
        self.assertEqual(obj.nome, "João da Silva")
        self.assertEqual(obj.telefone, "47 9 1234 5678")
        self.assertEqual(obj.data_nascimento, date(1976, 1, 1))