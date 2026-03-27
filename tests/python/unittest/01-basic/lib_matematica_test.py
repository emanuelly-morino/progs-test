import unittest
from lib_matematica import somar, fatorial

class TestMath(unittest.TestCase):

    def testar_soma(self):
        resultado = somar(2, 2)
        self.assertEqual(resultado, 4) #

    def testar_soma_negativa(self):
        resultado = somar(-1, -1)
        self.assertEqual(resultado, -2)

    def testar_fatorial(self):
        resultado = fatorial(5)
        self.assertEqual(resultado, 120)

    def testar_fatorial_zero(self):
        resultado = fatorial(0)
        self.assertEqual(resultado, 1)

    def testar_fatorial_negativo(self):
        resultado = fatorial(-1)
        self.assertEqual(resultado, -1)

if __name__ == '__main__':
    unittest.main()
