import unittest
import permstruct
from permstruct import *
import permstruct.dag
from permstruct.dag import *
import sys

class TestStruct(unittest.TestCase):
    def test_struct(self):

        struct([ Permutation([2,3,1]) ])

