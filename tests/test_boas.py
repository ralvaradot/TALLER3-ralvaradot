import unittest
from models.boa_constrictor import Boa_Constrictor

class Test_Boa(unittest.TestCase):
   
    def test_hacer_sonido(self):
        boa = Boa_Constrictor(nombre='pepa', peso=5.58, edad=4, kilos_comidos=1, paisorigen='Costa Rica', impuestos=1600)
        self.assertEqual(boa.hacer_sonido(), "¡Tssss!")

    def test_calcular_flete(self):
        boa = Boa_Constrictor('pepita', 6.75, 3, 1, 'Costa Rica', 1600)
        flete = 6.75 * 1600
        self.assertEqual(boa.calcular_flete(), flete)
        
    def test_adicionar_raton_comido(self):
        boa = Boa_Constrictor('pepita', 6.75, 3, 1, 'Costa Rica', 1600)
        for i in range(11):
            try:
                respuesta = boa.adicionar_raton_comido()
            except ValueError as e:
                respuesta = e.__str__()
            
        self.assertEqual(respuesta, "Demasiados Ratones!!")
        
            