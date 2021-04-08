import unittest
import sys
import os

ruta = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(ruta)

from src.blockchain import Bloque, Blockchain

class Test(unittest.TestCase):

    def test_es_bloque_deberia_de_ser_verdadero_cuando_mail_es_vacio(self):
        test = Blockchain()
        self.assertEqual(test.cadena[0].mail,"")


    def test_es_bloque_debe_ser_verdadero_cuando_index_es_cero(self):

        test = Blockchain()
        self.assertEqual(test.cadena[0].index, 0)

    def test_es_bloque_genesis_razon_debe_ser_verdadero_cuando_razon_es_vacio(self):
        test = Blockchain()
        self.assertEqual(test.cadena[0].razon,"")

    def test_is_bloque_genesis_hash_archivo_should_to_be_true_when_hash_archivo_is_string_cero(self):
        test = Blockchain()
        self.assertEqual(test.cadena[0].hashArchivo, "0")

    def test_is_bloque_genesis_hash_archivo_should_to_be_true_when_hash_anterior_archivo_is_string_cero(self):
        test = Blockchain()
        self.assertEqual(test.cadena[0].hashBlq, test.getHashByIndex(0))

        
if __name__ == '__main__':
    unittest.main() 