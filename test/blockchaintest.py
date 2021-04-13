import os
import sys
from datetime import datetime

import unittest

root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)

from src.blockchain import Blockchain
from src.bloque import Bloque

test = Blockchain()

class Test(unittest.TestCase):
    def test_is_bloque_should_to_be_true_when_bloque_is_created(self):
        test = Bloque(0, 'correo@prueba.com', 'prueba', 'hash_archivo', 'hash_anterior', '2021-04-11 21:00:00')
        test.setDateTimeString = '10'
        self.assertEqual(0, test.index)
        self.assertEqual("correo@prueba.com", test.correo)
        self.assertEqual("prueba", test.motivo)
        self.assertEqual("hash_archivo", test.hashArc)
        self.assertEqual("hash_anterior", test.hashAnt)
        self.assertEqual("2021-04-11 21:00:00", test.timestamp)
        self.assertEqual('a40bfe4dd0bf234716b76a3d5e75a40286e36b6849ccac735720151dc49c2662', test.hashBloque)
    
    def test_is_bloque_genesis_should_to_be_true_when_bloque_genesis_is_created(self):
        #test = Blockchain()
        self.assertEqual(0, test.cadena[0].index)
        self.assertEqual("", test.cadena[0].correo)
        self.assertEqual("", test.cadena[0].motivo)
        self.assertEqual("0", test.cadena[0].hashArc)
        self.assertEqual("0", test.cadena[0].hashAnt)
        self.assertEqual("2021-01-01 00:00:00", test.cadena[0].timestamp)
        self.assertEqual('efa3939f1f6768c242cb0e68ba9ad6cc10f10f7624f30a5cce51f640068b73c5', test.getHashByIndex(0))
    
    def test_is_bloque_One_should_to_be_true_when_bloque_One_is_created(self):
        test.crearBloque("correo@bloqueOne.com", "prueba", "hashArc")
        self.assertEqual(1, test.cadena[1].index)
        self.assertEqual("correo@bloqueOne.com", test.cadena[1].correo)
        self.assertEqual("prueba", test.cadena[1].motivo)
        self.assertEqual("hashArc", test.cadena[1].hashArc)
        self.assertEqual("efa3939f1f6768c242cb0e68ba9ad6cc10f10f7624f30a5cce51f640068b73c5", test.cadena[1].hashAnt)
        self.assertEqual("2021-01-01 22:00:00", test.cadena[1].timestamp)
        self.assertEqual('001dafe88b0d14e0cc71ce06947dd750f74a46c74d0fc0879484fa42a439b048', test.getHashByIndex(1))

    def test_si_singleton_debe_ser_verdadero_cuando_singleton_funcione(self):
         testSingleton1 = Blockchain()
         testSingleton2 = Blockchain()
         message = "El test del Singleton no funciona"
         self.assertTrue(id(testSingleton1) == id(testSingleton2), message)
if __name__ == '__main__':
    unittest.main()