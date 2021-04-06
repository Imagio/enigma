import unittest
from rotor import Rotor


class TestRotor(unittest.TestCase):

    def test_encrypt_A(self):
        rotor = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ")
        encrypted = rotor.encrypt("A")
        self.assertEqual("E", encrypted)

    def test_decrypt_A(self):
        rotor = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ")
        decrypted = rotor.decrypt("A")
        self.assertEqual("U", decrypted)
