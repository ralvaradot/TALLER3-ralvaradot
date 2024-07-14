import unittest
from models.huron import Huron

class TestHuron(unittest.TestCase):
    
    def test_hacer_sonido(self):
        huron = Huron(nombre='pepe', peso=3.85, edad=2, kilos_comidos=1, paisorigen='Mexico', impuestos=1200)
        self.assertEqual(huron.hacer_sonido(), "¡Eek Eek!")

    def test_calcular_flete(self):
        huron = Huron('pepito', 3.85, 2, 1, 'Mexico', 1200)
        flete = 3.85 * 1200
        self.assertEqual(huron.calcular_flete(), flete)
        