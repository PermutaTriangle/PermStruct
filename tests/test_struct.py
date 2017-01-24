import unittest
import permstruct
from permstruct import *
import permstruct.dag
from permstruct.dag import *
import sys

class TestStruct(unittest.TestCase):
    def test_struct_on_21(self):

        struct([ Permutation([2,1]) ], ask_verify_higher = False)

    def test_struct_on_231(self):

        struct([ Permutation([2,3,1]) ], ask_verify_higher = False)
