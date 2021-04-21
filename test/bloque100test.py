import unittest
import os
import sys
ruta = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(ruta)
from src.blockchain import Blockchain
from src.bloque import Bloque
class Bloques100Test(unittest.TestCase):
    def test_100Bloques_debe_ser_true_cuando_HashAnt_y_hashBloque_son_iguales_y_bloque_y_blockchainPos50_hashs_son_iguales(self):
        test = Blockchain()
        for i in range (100):
            test._Blockchain__crearBloque("alguien@gmail.com", "test", "hashArch", "2021-04-12 13:00:00")
        bloque49 = test.getBloqueByIndex(49)
        bloque50 = test.getBloqueByIndex(50)
        self.assertEqual(bloque50.hashAnt, bloque49.hashBloque)
        bloque = Bloque(50, "alguien@gmail.com", "test", "hashArch",test.getBloqueByIndex(49).hashBloque, "2021-04-12 13:00:00", 0)
        self.assertEqual(bloque.hashBloque, bloque50.hashBloque)

if __name__ == '__main__':
    unittest.main()