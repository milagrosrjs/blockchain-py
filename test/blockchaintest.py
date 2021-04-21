import os
import sys
from datetime import datetime
from bson import json_util
import json

import unittest

root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)

from src.blockchain import Blockchain
from src.bloque import Bloque

#Creo la blockchain global que sera usada en los test
test = Blockchain()
#Agregro bloque1 a la blockchain
test._Blockchain__crearBloque("correo@bloqueOne.com", "prueba", "hashArc", "2021-01-01 22:00:00")
#Agregro bloque2 a la blockchain
test._Blockchain__crearBloque("correo@bloqueOne.com", "pruebaBloque2", "hashArc", "2021-01-01 22:00:10")

class BlockchainTest(unittest.TestCase):
    
    def test_1_is_bloque_genesis_should_to_be_true_when_bloque_genesis_is_created(self):
        bloque0 = test.getBloqueByIndex(0)
        self.assertEqual(0, bloque0.index)
        self.assertEqual("", bloque0.correo)
        self.assertEqual("", bloque0.motivo)
        self.assertEqual("0", bloque0.hashArc)
        self.assertEqual("0", bloque0.hashAnt)
        self.assertEqual("2021-01-01 00:00:00", bloque0.timestamp)
        self.assertEqual('074c114814e06a532e2d1576e6b2263b150bd9ea7794b1e4db86f8a65281071a', test.getHashByIndex(0))
    
    def test_2_is_bloque_One_should_to_be_true_when_bloque_One_is_created(self):
        bloque1 = test.getBloqueByIndex(1)
        self.assertEqual(1, bloque1.index)
        self.assertEqual("correo@bloqueOne.com", bloque1.correo)
        self.assertEqual("prueba", bloque1.motivo)
        self.assertEqual("hashArc", bloque1.hashArc)
        self.assertEqual("074c114814e06a532e2d1576e6b2263b150bd9ea7794b1e4db86f8a65281071a", bloque1.hashAnt)
        self.assertEqual("2021-01-01 22:00:00", bloque1.timestamp)
        self.assertEqual('05972bdddaffebafb024ab5f22c3acd65a9e81c0d514277715e60d36cc479024', test.getHashByIndex(1))
    
    def test_3_is_bloque_Two_should_to_be_true_when_bloque_two_is_created(self):
        bloque2 = test.getBloqueByIndex(2)
        self.assertEqual(2, bloque2.index)
        self.assertEqual("correo@bloqueOne.com", bloque2.correo)
        self.assertEqual("pruebaBloque2", bloque2.motivo)
        self.assertEqual("hashArc", bloque2.hashArc)
        self.assertEqual("05972bdddaffebafb024ab5f22c3acd65a9e81c0d514277715e60d36cc479024", bloque2.hashAnt)
        self.assertEqual("2021-01-01 22:00:10", bloque2.timestamp)
        self.assertEqual('09063012d43b42aa3ef871e38571094bbb1dd5bb474911659a72d0d3ee521c4c', test.getHashByIndex(2))

    def test_4_is_bloque_by_hash_should_to_be_true_when_bloque_two_index_are_1(self):
        bloqueHash = test.getBlockByHash("074c114814e06a532e2d1576e6b2263b150bd9ea7794b1e4db86f8a65281071a")
        bloque = test.getBloqueByIndex(0)
        self.assertEqual(bloque, bloqueHash)

    def test_5_is_bloque_to_JSON_should_to_be_true_when_string_are_equals(self):
        bloque = test.getJsonBloqueByIndex(1)
        print(bloque)
        self.assertEqual(json.loads(bloque)["index"], 1)

if __name__ == '__main__': unittest.main()