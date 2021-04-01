import os
import sys

import unittest

root_folder = os.path.abspath(os.path.dirname(os.path.disrname(os.path.abspath(__file__))))
sys.path.append(root_folder)

from src.blockchain import Block

class Test(unittets.TestCase):
    def test_block(self):
        test = Block ("test@test.com", 1, "a")
        self.assertEqual(test.motivo, 1)

if __name__ == __main__:
    inittest.main()