import unittest
import problems.contadorVogais

class TestCalc(unittest.TestCase):
    def test_contar_vogais(self):
        self.assertEqual(problems.contadorVogais.contarVogais("Joao"), 3)
        self.assertEqual(problems.contadorVogais.contarVogais("Elefante"), 4)
        self.assertEqual(problems.contadorVogais.contarVogais("Pai"), 2)
        self.assertEqual(problems.contadorVogais.contarVogais("Cafe"), 2)
        self.assertEqual(problems.contadorVogais.contarVogais("Dono"), 2)
        self.assertEqual(problems.contadorVogais.contarVogais("Luana"), 3)



if __name__ == '__main__':
    unittest.main()



