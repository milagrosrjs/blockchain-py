import os
import sys
from datetime import datetime

import unittest

root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)

from src.blockchain import Blockchain
from src.bloque import Bloque

test = Blockchain()
    
class BloquesIgualesTest(unittest.TestCase):

    def test_dos_bloques_should_to_be_true_when_ambos_son_igual(self):
        bloque1 = Bloque(0, 'correo@prueba.com', 'prueba2BloquesIguales', 'hash_archivo', 'hash_anterior', '2021-04-11 21:00:00', 0)
        bloque2 = Bloque(0, 'correo@prueba.com', 'prueba2BloquesIguales', 'hash_archivo', 'hash_anterior', '2021-04-11 21:00:00', 0)
        self.assertEqual(bloque1.hashBloque, bloque2.hashBloque)

if __name__ == '__main__': unittest.main()