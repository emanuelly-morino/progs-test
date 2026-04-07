import unittest
from Servico import *

class TestarServico(unittest.TestCase):
    def test_criacao(self):
        obj = Servico("Troca de Óleo", 50)
        self.assertEqual(obj.descricao, "Troca de Óleo")
        self.assertEqual(obj.valor, 50)