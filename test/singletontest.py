import os
import sys
from datetime import datetime

import unittest

root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)

from src.blockchain import Blockchain
from src.bloque import Bloque

class SingletonTest(unittest.TestCase):

    def test_is_Singleton_should_to_be_true_when_Singleton_works(self):
            testSingleton1 = Blockchain()
            testSingleton2 = Blockchain()
            message = "Test Singleton doesn't works"
            self.assertTrue(id(testSingleton1) == id(testSingleton2), message)

if __name__ == '__main__': unittest.main()