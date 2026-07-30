# importar a biblioteca de testes
import unittest

from a_classes import *

# a classe de teste deve herdar de unittest.TestCase
class TestPessoa(unittest.TestCase):

    # nome do método de teste deve iniciar com 'test_'
    def test_criar_e_mostrar(self):
        p = Pessoa(1, "João da Silva", "jo@gmail.com")
        # aqui consiste no teste, 
        # comparando resultado esperado com o real
        self.assertEqual(p.nome, "João da Silva") 
        self.assertEqual(p.email, "jo@gmail.com")

class TestCelular(unittest.TestCase):
    def test_criar_e_mostrar(self):
        p = Pessoa(1, "João da Silva", "jo@gmail.com")
        c = Celular(1, "47 9 1234 4321", "Motorola", "Vivo", p)

        self.assertEqual(c.pessoa.nome, "João da Silva")
        self.assertEqual(c.marca, "Motorola")

if __name__ == '__main__':
    # executa os testes
    unittest.main()

'''
python3 -m unittest -v c_teste_automatizado.py 
'''