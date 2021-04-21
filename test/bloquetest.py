import os
import sys
from datetime import datetime

import unittest

root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)

from src.blockchain import Blockchain
from src.bloque import Bloque

class BloqueTest(unittest.TestCase):
    def test_sera_true_cuando_bloque_es_creado(self):
        test = Bloque(0, 'correo@prueba.com', 'prueba', 'hash_archivo', 'hash_anterior', '2021-04-11 21:00:00', 0)
        test.setDateTimeString = '10'
        self.assertEqual(0, test.index)
        self.assertEqual("correo@prueba.com", test.correo)
        self.assertEqual("prueba", test.motivo)
        self.assertEqual("hash_archivo", test.hashArc)
        self.assertEqual("hash_anterior", test.hashAnt)
        self.assertEqual("2021-04-11 21:00:00", test.timestamp)
        self.assertEqual('0887a185101a6b5cbd5716d75ec940f5438ebf1f067f5ced2f62c668fb45eb12', test.hashBloque)

if __name__ == '__main__':
    unittest.main()