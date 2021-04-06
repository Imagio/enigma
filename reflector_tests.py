import unittest
from reflector import Reflector


class TestReflector(unittest.TestCase):

    def test_reflect_A(self):
        reflector = Reflector("EJMZALYXVBWFCRQUONTSPIKHGD")
        encrypted = reflector.encrypt("A")
        self.assertEqual("E", encrypted)

    def test_reflect_E(self):
        reflector = Reflector("EJMZALYXVBWFCRQUONTSPIKHGD")
        encrypted = reflector.encrypt("E")
        self.assertEqual("A", encrypted)
